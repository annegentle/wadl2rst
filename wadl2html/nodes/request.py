from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class RequestNode(BaseNode):
    template = templates['request']