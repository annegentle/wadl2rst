
from unittest import TestCase

from wadl2rst import tree
from wadl2rst.transformations.cleanup_application_node import cleanup_application_node


class CleanupApplicationNodeTest(TestCase):

    def setUp(self):
        self.root_node = tree.xml_string_to_tree(test_xml)
        cleanup_application_node(self.root_node)

    def test_only_requests(self):
        names = [c.attributes.get("name", None) for c in self.root_node.children]
        self.assertIn('resources', names)
        self.assertNotIn('method', names)
        self.assertNotIn('params', names)


test_xml = """
<application>
    <resources name="resources" />
    <method name="method" />
    <params name="params" />
</application>
"""
