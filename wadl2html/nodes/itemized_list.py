
from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class ItemizedListNode(BaseNode):
    template = templates['itemized_list']
