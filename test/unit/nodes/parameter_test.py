
from unittest import TestCase

from wadl2rst.nodes.char import CharNode
from wadl2rst.nodes.parameter import ParameterNode


class TestParameterNode(TestCase):

    def setUp(self):
        self.attributes = {"name": "test_name", "type": "test_type"}
        self.node = ParameterNode(None, "parameter", self.attributes)
        self.node.children.append(CharNode(None, "test_data"))

    def test_get_table_row(self):
        output = self.node.get_table_row()
        self.assertIn("test_name", output)
        self.assertIn("test_type", output)
        self.assertIn("test_data", output)

    def test_format_template_type_names(self):
        self.node.attributes['style'] = 'template'
        output = self.node.get_table_row()
        self.assertIn("{test_name}", output)
