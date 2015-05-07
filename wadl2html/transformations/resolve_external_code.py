
import functools
import os

import pygments
from pygments import lexers
from pygments import formatters

from wadl2html.nodes.char import CharNode


def resolve_external_code(base_path, tree):
    """ Resolve the code that <xsdxt:code> nodes refer to. """

    # find all the code nodes
    code_nodes = []
    code_visitor = functools.partial(find_code_nodes, code_nodes)
    tree.visit(code_visitor)

    for node in code_nodes:
        # grab the file location
        href = node.attributes['href']
        path = os.path.normpath(os.path.join(base_path, href))

        # grab the type of the file
        mimetype = node.parent.parent.attributes.get('mediaType', None)
        if mimetype is None:
            continue

        # grab the file contents
        text = ""
        with open(path, 'r') as f:
            text = f.read()

        # format the file contents
        lexer = lexers.get_lexer_for_mimetype(mimetype)
        formatter = formatters.get_formatter_by_name("html")
        output = pygments.highlight(text, lexer, formatter)

        # create a node with the contents and put it into the file
        output_node = CharNode(node.parent, output)
        node.parent.add_child(output_node)

        # remove the xsdxt node from the parent
        node.parent.remove_child(node)
        node.parent = None


def find_code_nodes(memory, node):
    if node.name == "xsdxt:code":
        memory.append(node)
