
import functools

from unittest import TestCase

from wadl2html.nodes.base import BaseNode


class TestBaseNode(TestCase):

    def setUp(self):
        self.single_node = FakeNode(None, "test", {})

        self.parent_node = FakeNode(None, "parent", {})
        self.child_node = FakeChildNode(self.parent_node, "child", {})
        self.parent_node.children.append(self.child_node)

    def test_should_remove_child(self):
        self.parent_node.remove_child(self.child_node)
        self.assertEquals(0, len(self.parent_node.children))

    def test_should_render_no_children(self):
        result = self.single_node.to_html()
        self.assertEquals("hello", result)

    def test_should_render_with_children(self):
        result = self.parent_node.to_html()
        self.assertEquals("hello world", result)

    def test_should_handle_attributes(self):
        node = FakeAttributeNode(None, "test", {'foo': 'bar'})
        result = node.to_html()
        self.assertEquals("bar", result)

    def test_should_find_first_no_results(self):
        result = self.parent_node.find_first("no")
        self.assertEquals(result, None)

    def test_should_clone_attributes(self):
        clone = self.parent_node.clone()
        self.assertEquals(self.parent_node.name, clone.name)
        self.assertEquals(self.child_node.name, clone.children[0].name)

    def test_clone_should_have_different_pointers(self):
        clone = self.parent_node.clone()
        self.assertNotEquals(id(self.parent_node), id(clone))
        self.assertNotEquals(id(self.child_node), id(clone.children[0]))

    def test_visitor_should_visit_nodes(self):
        nodes = []
        func = functools.partial(fake_visit, nodes)

        self.parent_node.visit(func)
        self.assertIn(self.parent_node, nodes)
        self.assertIn(self.child_node, nodes)

#
# Fakes for Testing Purposes
#

class FakeNode(BaseNode):
    template = "hello{{child_html}}"


class FakeChildNode(BaseNode):
    template = " world"


class FakeAttributeNode(BaseNode):
    template = "{{attributes['foo']}}"


def fake_visit(memory, node):
    memory.append(node)
