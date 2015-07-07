
import re

from wadl2rst.nodes.base import BaseNode

COMMA_CLEANUP = re.compile("[\s]+(?P<foo>,.)")


class ParaNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        child_rst = " ".join([child.to_rst() for child in self.children])

        # collapse any strings of whitespace into a single space
        child_rst = ' '.join(child_rst.split())

        # remove any whitespace before punctuation.
        child_rst = COMMA_CLEANUP.sub(r"\1", child_rst)

        return child_rst + "\n\n"
