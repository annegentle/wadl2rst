
from wadl2html.nodes.base import BaseNode


class CharNode(BaseNode):

    def __init__(self, parent, text):
        super(CharNode, self).__init__(parent, "char", {})
        self.text = text

    def to_html(self):
        return self.text
