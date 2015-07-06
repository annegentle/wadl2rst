
import functools

from unittest import TestCase

from wadl2rst.nodes.char import CharNode


class TestCharNode(TestCase):

    def setUp(self):
        self.node = CharNode(None, "foo")

    def test_create_char_node(self):
        self.assertEquals(self.node.attributes['text'], 'foo')

    def test_handle_clone_properly(self):
        clone = self.node.clone()
        self.assertEquals(self.node.attributes, clone.attributes)
        self.assertNotEquals(id(self.node), id(clone))
