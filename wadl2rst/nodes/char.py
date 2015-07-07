
from wadl2rst.nodes.base import BaseNode


class CharNode(BaseNode):

    def __init__(self, parent, text):
        super(CharNode, self).__init__(parent, "char", {'text': text})

    def clone(self):
        clone = self.__class__(self.parent, self.attributes['text'])
        clone.children = [c.clone() for c in self.children]
        return clone

    def to_rst(self):
        return self.attributes['text'].strip()
