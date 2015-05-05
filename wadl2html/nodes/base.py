
import jinja2

from wadl2html.templates import templates


class BaseNode(object):
    """ Base Node. This represents a node in the html output. """

    template = templates['base_node']

    def __init__(self, parent, name, attributes):
        self.parent = parent
        self.name = name
        self.attributes = attributes
        self.children = []

    def replace_child(self, old_child, new_child):
        idx = self.children.index(old_child)
        self.children.insert(idx, new_child)
        self.remove_child(old_child)

    def remove_child(self, child):
        self.children.remove(child)

    def visit(self, function):
        """ Execute a function against this node and each of it's children. """

        for child in self.children:
            child.visit(function)

        function(self)

    def to_html(self):
        """ Return the html representation of this tag and it's children. """

        child_html = ""

        # render all of the children of this node first
        for child in self.children:
            child_html += child.to_html()

        template = jinja2.Template(self.template)
        return template.render(node_name=self.name,
                               attributes=self.attributes,
                               child_html=child_html)
