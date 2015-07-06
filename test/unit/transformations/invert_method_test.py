
from unittest import TestCase

from wadl2rst import tree
from wadl2rst.transformations.collapse_resources import collapse_resources
from wadl2rst.transformations.invert_method import invert_method


class InvertMethodTest(TestCase):

    def setUp(self):
        self.root_node = tree.xml_string_to_tree(example_xml)
        collapse_resources(self.root_node)
        invert_method(self.root_node)

        self.resources = self.root_node.find_first("resources")
        self.method = self.root_node.find_first("method")

    def test_resources_tag_should_only_have_methods(self):
        names = [node.name for node in self.resources.children]
        self.assertEquals(len(names), 1)
        self.assertIn("method", names)
        self.assertNotIn("resource", names)

    def test_method_should_contain_a_resource(self):
        names = [node.name for node in self.method.children]
        self.assertEquals(len(names), 1)
        self.assertIn("resource", names)

    def test_resource_should_have_methods_removed(self):
        resource = self.method.children[0]
        names = [node.name for node in resource.children]
        self.assertNotIn("method", names)

    def test_method_resource_should_have_params(self):
        resource = self.method.children[0]
        names = [node.name for node in resource.children]
        self.assertIn("params", names)


example_xml = """
<root>
  <resources>
    <resource path="foo">
      <resource path="foo_id">
        <param name="foo_id" />
        <resource path="bar">
          <method name="test_method"/>
        </resource>
        <resource path="baz" />
      </resource>
    </resource>
  </resources>
</root>
"""
