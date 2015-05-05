
from wadl2html.nodes.base import BaseNode


class CharNode(BaseNode):

    template = "{{attributes['text']}}"

    def __init__(self, parent, text):
        super(CharNode, self).__init__(parent, "char", {'text': text})
