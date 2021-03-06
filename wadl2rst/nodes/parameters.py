
from wadl2rst import table
from wadl2rst.nodes.base import BaseNode


class ParametersNode(BaseNode):

    def to_keypairs(self, style=None):
        params = self.get_params(style)

        if not params:
            return u''

        output = u''
        for param in params:
            output += "  - %s: %s\n" % (
                param.attributes.get('name', ''),
                param.attributes.get('name', ''))

        return output

    def to_table(self, style=None):
        """ Create a table from these params """

        columns = ["Name", "Type", "Description"]
        rows = [item.get_table_row() for item in self.get_params(style)]

        if len(rows) > 0:
            return table.create_table(columns, rows)
        else:
            return None

    def get_params(self, style):
        output = []

        for node in self.children:
            if node.name != "param":
                continue

            if (style is not None) and (node.attributes.get('style', None) != style):
                continue

            output.append(node)

        return output
