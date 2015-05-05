
import os
import xml.parsers.expat

from wadl2html.nodes.application import ApplicationNode
from wadl2html.nodes.base import BaseNode
from wadl2html.nodes.char import CharNode
from wadl2html.nodes.code import CodeNode
from wadl2html.nodes.para import ParaNode
from wadl2html.nodes.url_parameter import UrlParameterNode
from wadl2html.nodes.url_parameters import UrlParametersNode


class ParserState(object):

    node_mapping = {
        "application": ApplicationNode,
        "code": CodeNode,
        "replaceable": BaseNode,
        "doc": BaseNode,
        "grammars": BaseNode,
        "include": BaseNode,
        "method": BaseNode,
        "para": ParaNode,
        "param": UrlParameterNode,
        "params": UrlParametersNode,
        "paramenter": BaseNode,
        "representation": BaseNode,
        "request": BaseNode,
        "resource": BaseNode,
        "resources": BaseNode,
        "response": BaseNode,
        "root": BaseNode,
        "wadl:doc": BaseNode,
        "xsdxt:code": BaseNode,
    }

    def __init__(self):
        self.root = BaseNode(None, "root", {})
        self.current = self.root

    def start_element(self, name, attrs):
        if name in self.node_mapping:
            node = self.node_mapping[name](self.current, name, attrs)
        else:
            node = BaseNode(self.current, name, attrs)

        self.current.children.append(node)
        self.current = node

    def end_element(self, name):
        self.current = self.current.parent

    def char_data(self, data):
        if data.strip() != "":
            node = CharNode(self.current, data)
            self.current.children.append(node)

    def entity_data(self, entityName, is_parameter_entity, value, base, systemId, publicId, notationName):
        pass

    def default(self, data):
        pass


def xml_to_tree(input_xml):
    """ Parse the XML into our intermediate representation. """

    state = ParserState()
    parser = xml.parsers.expat.ParserCreate()
    parser.StartElementHandler = state.start_element
    parser.EndElementHandler = state.end_element
    parser.CharacterDataHandler = state.char_data
    parser.EntityDeclHandler = state.entity_data
    parser.DefaultHandler = state.default
    parser.ParseFile(input_xml)

    if len(state.root.children) == 0:
        return None

    return state.root.children[0]
