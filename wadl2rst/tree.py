
import xml.parsers.expat

from wadl2rst.nodes.base import BaseNode
from wadl2rst.nodes.char import CharNode
from wadl2rst.nodes.code import CodeNode
from wadl2rst.nodes.itemized_list import ItemizedListNode
from wadl2rst.nodes.link import LinkNode
from wadl2rst.nodes.list_item import ListItemNode
from wadl2rst.nodes.method import MethodNode
from wadl2rst.nodes.note import NoteNode
from wadl2rst.nodes.para import ParaNode
from wadl2rst.nodes.parameter import ParameterNode
from wadl2rst.nodes.parameters import ParametersNode
from wadl2rst.nodes.representation import RepresentationNode


class ParserState(object):

    node_mapping = {
        "code": CodeNode,
        "replaceable": CodeNode,
        "command": CodeNode,
        "errorcode": CodeNode,
        "itemizedlist": ItemizedListNode,
        "link": LinkNode,
        "listitem": ListItemNode,
        "method": MethodNode,
        "note": NoteNode,
        "para": ParaNode,
        "param": ParameterNode,
        "params": ParametersNode,
        "parameter": CodeNode,
        "representation": RepresentationNode,
        "literal": CodeNode,
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
