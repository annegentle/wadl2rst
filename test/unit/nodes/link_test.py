
from unittest import TestCase

from wadl2rst.nodes.char import CharNode
from wadl2rst.nodes.link import LinkNode


class TestLinkNode(TestCase):

    def setUp(self):
        self.node = LinkNode(None, "link", {"xlink:href": "href"})
        self.text = CharNode(None, "text")
        self.node.children.append(self.text)

    def test_to_rst(self):
        expected = "`text <href>`__"
        self.assertEquals(expected, self.node.to_rst())
