
from unittest import TestCase

from wadl2rst import tree
from wadl2rst.transformations.wrap_response_elements import wrap_response_elements


class WrapResponseElementsTest(TestCase):

    def test_wrapped_no_responses(self):
        self.root_node = tree.xml_string_to_tree(test_no_responses_xml)
        wrap_response_elements(self.root_node)

        responses = self.root_node.find_first("responses")
        self.assertTrue(responses is not None)

        names = [c.attributes.get("name", None) for c in responses.children]
        self.assertIn("foo", names)
        self.assertIn("bar", names)

    def test_wrapped_with_responses(self):
        self.root_node = tree.xml_string_to_tree(test_with_params_xml)
        wrap_response_elements(self.root_node)

        responses = self.root_node.find_first("responses")
        self.assertTrue(responses is not None)

        names = [c.attributes.get("name", None) for c in responses.children]
        self.assertIn("foo", names)
        self.assertIn("bar", names)


test_no_responses_xml = """
<root>
    <response name="foo" />
    <response name="bar" />
</root>
"""


test_with_responses_xml = """
<root>
    <responses>
        <response name="foo" />
    </responses>
    <response name="bar" />
</root>
"""
