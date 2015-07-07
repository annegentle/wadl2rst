
from unittest import TestCase

from wadl2rst import tree
from wadl2rst.transformations.resolve_internal import resolve_internal


class ResolveInternalTest(TestCase):

    def setUp(self):
        self.root_node = tree.xml_string_to_tree(example_xml)
        resolve_internal(self.root_node)

    def test_should_add_target_to_new_position(self):
        container = self.root_node.find_first("container")
        self.assertEquals(container.children[0].name, "target")

    def test_should_remove_link_tag(self):
        container = self.root_node.find_first("container")
        self.assertEquals(len(container.children), 1)

    def test_should_remove_targets_from_old_place(self):
        self.assertEquals(len(self.root_node.children), 1)


example_xml = """
<root>
  <container>
    <link href="#foo" />
  </container>
  <target id="foo" />
</root>
"""
