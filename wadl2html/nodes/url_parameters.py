
from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class UrlParametersNode(BaseNode):
    template = templates['url_parameters']
