
from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class ParameterNode(BaseNode):

    def get_table_row(self):
        type = self.attributes.get('type', '')

        name = self.attributes.get('name', '')
        if self.attributes.get('style', '') == "template":
            name = "{" + name + "}"

        return [name, type, self.to_rst()]
