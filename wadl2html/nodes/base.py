
import jinja2

from wadl2html.templates import templates


class BaseNode(object):
    """ Base Node. This represents a node in the html output. """

    template = templates['base_node']

    def __init__(self, parent, attributes):
        self.parent = parent
        self.attributes = attributes
        self.children = []

    def to_html(self):
        """ Return the html representation of this tag and it's children. """

        child_html = ""

        # render all of the children of this node first
        for child in self.children:
            child_html += child.to_html()

        template = jinja2.Template(self.template)
        return template.render(attributes=self.attributes,
                               child_html=child_html)
