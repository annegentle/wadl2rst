
import functools

from unittest import TestCase

from wadl2rst.nodes.method import MethodNode


class TestMethodNode(TestCase):

    def setUp(self):
        self.node = MethodNode(None, "foo")
