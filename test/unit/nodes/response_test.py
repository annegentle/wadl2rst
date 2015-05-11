
import functools

from unittest import TestCase

from wadl2html.nodes.response import ResponseNode


class TestResponseNode(TestCase):

    def setUp(self):
        self.node = ResponseNode(None, "foo")
