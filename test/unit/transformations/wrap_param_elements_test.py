
from unittest import TestCase

from wadl2rst import tree
from wadl2rst.transformations.wrap_param_elements import wrap_param_elements


class WrapParamElementsTest(TestCase):

    def test_wrapped_no_params(self):
        self.root_node = tree.xml_string_to_tree(test_no_params_xml)
        wrap_param_elements(self.root_node)

        parameters = self.root_node.find_first("params")
        self.assertTrue(parameters is not None)

        names = [c.attributes.get("name", None) for c in parameters.children]
        self.assertIn("foo", names)
        self.assertIn("bar", names)

    def test_wrapped_with_params(self):
        self.root_node = tree.xml_string_to_tree(test_with_params_xml)
        wrap_param_elements(self.root_node)

        parameters = self.root_node.find_first("params")
        self.assertTrue(parameters is not None)

        names = [c.attributes.get("name", None) for c in parameters.children]
        self.assertIn("foo", names)
        self.assertIn("bar", names)


test_no_params_xml = """
<root>
    <param name="foo" />
    <param name="bar" />
</root>
"""


test_with_params_xml = """
<root>
    <params>
        <param name="foo" />
    </params>
    <param name="bar" />
</root>
"""
