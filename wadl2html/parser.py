
import os
import xml.parsers.expat

from wadl2html.nodes.base import BaseNode
from wadl2html.nodes.char import CharNode


class ParserState(object):

    node_mapping = {}

    def __init__(self):
        self.root = BaseNode(None, "root", {})
        self.current = self.root

    def start_element(self, name, attrs):
        print "start_element: {}, {}".format(name, attrs)

        if name in self.node_mapping:
            node = self.node_mapping[name](self.current, attrs)
        else:
            node = BaseNode(self.current, name, attrs)

        self.current.children.append(node)
        self.current = node

    def end_element(self, name):
        print "end_element: {}".format(name)
        self.current = self.current.parent

    def char_data(self, data):
        if data.strip() != "":
            print "char_data: {}".format(data)
            node = CharNode(self.current, data)
            self.current.children.append(node)

    def entity_data(self, entityName, is_parameter_entity, value, base, systemId, publicId, notationName):
        data = [entityName, is_parameter_entity, value, base, systemId, publicId, notationName]
        print "entity_data: {}".format(data)

    def default(self, data):
        print "default: {}".format(data)


def parse_xml(input_xml):

    state = ParserState()
    parser = xml.parsers.expat.ParserCreate()
    parser.StartElementHandler = state.start_element
    parser.EndElementHandler = state.end_element
    parser.CharacterDataHandler = state.char_data
    parser.EntityDeclHandler = state.entity_data
    parser.DefaultHandler = state.default
    parser.ParseFile(input_xml)
    return state.root

def parse_wadl(input_xml):
    """ Parse the wadl into nodes. We'll do this in multiple passes. """

    # take the xml and turn it into a tree of nodes to process
    tree = parse_xml(input_xml)

    # resolve internal references

    return tree
