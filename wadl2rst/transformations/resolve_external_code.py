
from __future__ import print_function

import functools
import os
import sys

from wadl2rst.nodes.char import CharNode


def resolve_external_code(base_path, tree, samples_path):
    """ Resolve the code that <xsdxt:code> nodes refer to. """

    # find all the code nodes
    code_nodes = []
    code_visitor = functools.partial(find_code_nodes, code_nodes)
    tree.visit(code_visitor)

    # build the api-samples path
    for node in code_nodes:
        if 'href' in node.attributes:
            href = node.attributes['href']
            href_split = href.split('/')
            text = os.path.normpath(os.path.join(samples_path, href_split[-2], href_split[-1]))
        else:
            # don't try to return any samples data
            text = None

        # create a node with the contents and put it into the file
        output_node = CharNode(node.parent, text)
        node.parent.add_child(output_node)

        node.parent.remove_child(node)
        node.parent = None


def get_file_contents(file):
    try:
        with open(file, 'r') as f:
            return f.read()
    except IOError, e:
        print("Error getting external file {}: {}".format(file, e.strerror), file=sys.stderr)
        return ""


def get_inline_code(node):
    return node.to_rst()


def get_media_type(node):
    mimetype = node.attributes.get('mediaType', None)

    if mimetype is not None:
        return mimetype

    if node.parent is None:
        return "text/plain"

    return get_media_type(node.parent)


def find_code_nodes(memory, node):
    if node.name == "xsdxt:code":
        memory.append(node)


# map of mimetype issues
mimetype_translation = {
    "text/json": "application/json",
    "application/text": "text/plain",
    "application/http": "text/plain",
    "application/atom-xml": "application/xml",
    "application/octet-stream": "text/plain",
    "application/vnd.rackspace.incident-v1+xml": "application/xml"
}
