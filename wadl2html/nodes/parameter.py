
from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class ParameterNode(BaseNode):
    template = templates['parameter']
