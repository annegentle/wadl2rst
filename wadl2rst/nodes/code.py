
from wadl2rst.nodes.base import BaseNode


class CodeNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        child_rst = " ".join([child.to_rst() for child in self.children])
        return "``" + child_rst + "``"
