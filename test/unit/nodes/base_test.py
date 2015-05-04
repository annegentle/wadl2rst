
from unittest import TestCase

from wadl2html.nodes.base import BaseNode


class TestBaseNode(TestCase):

    def test_should_render_no_children(self):
        node = FakeNode(None, {})
        result = node.to_html()
        self.assertEquals("hello", result)

    def test_should_render_with_children(self):
        parent_node = FakeNode(None, {})
        child_node = FakeChildNode(parent_node, {})
        parent_node.children.append(child_node)

        result = parent_node.to_html()
        self.assertEquals("hello world", result)

    def test_should_handle_attributes(self):
        node = FakeAttributeNode(None, {'foo': 'bar'})
        result = node.to_html()
        self.assertEquals("bar", result)

#
# Fakes for Testing Purposes
#

class FakeNode(BaseNode):
    template = "hello{{child_html}}"


class FakeChildNode(BaseNode):
    template = " world"


class FakeAttributeNode(BaseNode):
    template = "{{attributes['foo']}}"
