
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
        mimetype = get_media_type(node)
        if mimetype is None:
            continue

        # TODO: if we have many more exceptions, do something cleaner instead.
        if mimetype == "text/json":
            mimetype = "application/json"

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

        node.parent.remove_child(node)
        node.parent = None


def get_media_type(node):
    mimetype = node.attributes.get('mediaType', None)

    if mimetype is not None:
        return mimetype

    if node.parent is None:
        return None

    return get_media_type(node.parent)


def find_code_nodes(memory, node):
    if node.name == "xsdxt:code":
        memory.append(node)
