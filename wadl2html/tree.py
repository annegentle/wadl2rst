
import os
import xml.parsers.expat

from wadl2html.nodes.application import ApplicationNode
from wadl2html.nodes.base import BaseNode
from wadl2html.nodes.char import CharNode
from wadl2html.nodes.code import CodeNode
from wadl2html.nodes.itemized_list import ItemizedListNode
from wadl2html.nodes.link import LinkNode
from wadl2html.nodes.list_item import ListItemNode
from wadl2html.nodes.method import MethodNode
from wadl2html.nodes.note import NoteNode
from wadl2html.nodes.para import ParaNode
from wadl2html.nodes.parameter import ParameterNode
from wadl2html.nodes.parameters import ParametersNode
from wadl2html.nodes.request import RequestNode
from wadl2html.nodes.responses import ResponsesNode
from wadl2html.nodes.response import ResponseNode
from wadl2html.nodes.wadl_doc import WadlDocNode
from wadl2html.nodes.xsdxt_code import XsdxtCodeNode


class ParserState(object):

    node_mapping = {
        "application": ApplicationNode,
        "code": CodeNode,
        "replaceable": CodeNode,
        "command": CodeNode,
        "errorcode": CodeNode,
        "grammars": BaseNode,
        "include": BaseNode,
        "itemizedlist": ItemizedListNode,
        "link": LinkNode,
        "listitem": ListItemNode,
        "method": MethodNode,
        "note": NoteNode,
        "para": ParaNode,
        "param": ParameterNode,
        "params": ParametersNode,
        "parameter": CodeNode,
        "representation": BaseNode,
        "request": BaseNode,
        "resource": BaseNode,
        "resources": BaseNode,
        "response": ResponseNode,
        "responses": ResponsesNode,
        "request": RequestNode,
        "root": BaseNode,
        "literal": CodeNode,
        "wadl:doc": WadlDocNode,
        "warning": CodeNode
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


def xml_file_to_tree(input_xml):
    """ Parse the XML File into our intermediate representation. """

    parser, state = setup_parser_and_state()
    parser.ParseFile(input_xml)

    if len(state.root.children) == 0:
        return None

    return state.root.children[0]


def xml_string_to_tree(input_xml):
    """ Parse the XML string into our intermediate representation. """

    parser, state = setup_parser_and_state()
    parser.Parse(input_xml, True)

    if len(state.root.children) == 0:
        return None

    return state.root.children[0]


def setup_parser_and_state():
    """ Return a configured parser and state objects. """

    state = ParserState()
    parser = xml.parsers.expat.ParserCreate()
    parser.StartElementHandler = state.start_element
    parser.EndElementHandler = state.end_element
    parser.CharacterDataHandler = state.char_data
    parser.EntityDeclHandler = state.entity_data
    parser.DefaultHandler = state.default

    return (parser, state)
