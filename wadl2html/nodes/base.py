
import functools


class BaseNode(object):
    """ Base Node. This represents a node in the html output. """

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

    def find(self, name):
        # TODO: use everywhere
        nodes = []

        def finder(node):
            if (node.name == name):
                nodes.append(node)

        self.visit(finder)
        return nodes

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
            for child in self.children:
                if child.name == name:
                    return child

        for child in self.children:
            output = child.find_one_of(names)
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

    def to_rst(self):
        """ Return the html representation of this tag and it's children. """

        child_rst = "".join([child.to_rst() for child in self.children])
        return child_rst

    def __repr__(self):
        class_name = self.__class__.__name__
        return "<{} name='{}' attributes='{}'>".format(class_name, self.name, self.attributes)
