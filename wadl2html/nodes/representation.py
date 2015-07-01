
from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class RepresentationNode(BaseNode):

    def to_example(self):
        code_node = self.find_first("xsdxt:sample")

        if code_node is None:
            return None

        char_node = code_node.find_first("char")

        if char_node is None:
            return None

        code_text = char_node.attributes['text']
        output = ["    " + line for line in code_text.split("\n")]

        return {
            "type": self.attributes['mediaType'],
            "code": "\n".join(output)
        }
