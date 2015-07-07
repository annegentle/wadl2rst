
from unittest import TestCase

from wadl2rst import tree
from wadl2rst.transformations.collapse_resources import collapse_resources


class CollapseResourcesTest(TestCase):

    def setUp(self):
        self.root_node = tree.xml_string_to_tree(example_xml)
        collapse_resources(self.root_node)
        self.resource = self.root_node.find_first("resource")

    def test_should_collapse_resources(self):
        child_names = [node.name for node in self.resource.children]
        self.assertNotIn("resource", child_names)

    def test_should_only_keep_resources_with_methods(self):
        resources = self.root_node.find_first("resources")
        self.assertEquals(1, len(resources.children))

    def test_should_record_path_properly(self):
        self.assertEquals("/foo/foo_id/bar",
                          self.resource.attributes['full_path'])

    def test_should_keep_intermediate_params(self):
        self.assertEquals(2, len(self.resource.children))
        params = self.resource.children[0]
        self.assertEquals("params", params.name)
        self.assertEquals("foo_id", params.children[0].attributes['name'])


example_xml = """
<root>
  <resources>
    <resource path="foo">
      <resource path="foo_id">
        <param name="foo_id" />
        <resource path="bar">
          <method />
        </resource>
        <resource path="baz" />
      </resource>
    </resource>
  </resources>
</root>
"""
