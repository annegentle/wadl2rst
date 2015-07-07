
from wadl2rst.nodes.base import BaseNode


class ParameterNode(BaseNode):

    def get_table_row(self):
        param_type = self.attributes.get('type', '')
        name = self.attributes.get('name', '')

        if self.attributes.get('style', '') == "template":
            name = "{" + name + "}"

        necessity = self.attributes.get('required', None)
        if necessity is not None:
            necessity = 'Required' if necessity else 'Optional'
            param_type += " *({})*".format(necessity)

        return [name, param_type, self.to_rst()]
