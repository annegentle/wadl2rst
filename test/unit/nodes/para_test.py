
from unittest import TestCase

from wadl2rst.nodes.char import CharNode
from wadl2rst.nodes.para import ParaNode


class TestParaNode(TestCase):

    def setUp(self):
        self.node = ParaNode(None, "para", {})

    def test_to_rst(self):
        self.node.children.append(CharNode(None, "text"))
        self.assertEquals("text\n\n", self.node.to_rst())

    def test_collapse_spaces(self):
        self.node.children.append(CharNode(None, "text  with   spaces"))
        self.assertEquals("text with spaces\n\n", self.node.to_rst())

    def test_no_spaces_before_punctuation(self):
        self.node.children.append(CharNode(None, "text , other ."))
        self.assertEquals("text, other.\n\n", self.node.to_rst())
