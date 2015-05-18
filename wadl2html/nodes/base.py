
import jinja2

from wadl2html.templates import templates


class BaseNode(object):
    """ Base Node. This represents a node in the html output. """

    template = templates['default']

    def __init__(self, parent, name, attributes):
        self.parent = parent
        self.name = name
        self.attributes = attributes
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def replace_child(self, old_child, new_child):
        idx = self.children.index(old_child)
        self.children.insert(idx, new_child)
        self.remove_child(old_child)

    def clone(self):
        clone = self.__class__(self.parent, self.name, self.attributes)

        for node in self.children:
            child = node.clone()
            clone.add_child(child)
            child.parent = clone

        return clone

    def find_first(self, name):
        """ Do a breadth-first search for a node with the specified name. """

        for child in self.children:
            if child.name == name:
                return child

        for child in self.children:
            response = child.find_first(name)
            if response is not None:
                return response

        return None

    def find_one_of(self, names):
        """ Find the first of a set of tags. """

        output = None

        for name in names:
            output = self.find_first(name)
            if output is not None:
                return output

        raise ValueError("No child nodes found with names: {} for node with attributes: {}".format(
            names, self.attributes))

    def visit(self, function):
        """ Execute a function against this node and each of it's children in a
        breadth-first manner. """

        function(self)

        for child in self.children:
            child.visit(function)

    def to_html(self):
        """ Return the html representation of this tag and it's children. """

        child_html = " ".join([child.to_html() for child in self.children])

        template = jinja2.Template(self.template)
        return template.render(node=self,
                               node_name=self.name,
                               attributes=self.attributes,
                               child_html=child_html)
