
from wadl2rst.nodes.base import BaseNode


class LinkNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        child_rst = "".join([child.to_rst() for child in self.children])
        href = self.attributes.get("href")

        if href is None:
            href = self.attributes.get("xlink:href")

        return "`{} <{}>`__".format(child_rst, href)
