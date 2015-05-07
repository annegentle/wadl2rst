
from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class WadlDocNode(BaseNode):
    template = templates['wadl_doc']
