
import functools


def resolve_internal(tree):
    """ Given a tree, replace any nodes with an 'href' attribute
    with the node with a corresponding 'id'. """

    # get all the nodes with an id attribute
    id_map = {}
    id_visitor = functools.partial(get_id_nodes, id_map)
    tree.visit(id_visitor)

    # get all the nodes with an href attribute
    href_nodes = []
    href_visitor = functools.partial(get_href_nodes, href_nodes)
    tree.visit(href_visitor)

    # replace each node in the href map with a node in the id map
    for href_node in href_nodes:
        key = href_node.attributes["href"].strip('#')

        # grab the id node associated with the href node
        id_node = id_map.get(key, None)
        if id_node is None:
            continue

        # since this node is used by-reference, we'll remove it from where it's defined
        if id_node.parent is not None:
            id_node.parent.remove_child(id_node)
            id_node.parent = None

        new_node = id_node.clone()

        # replace the href_node with the id_node
        href_node.parent.replace_child(href_node, new_node)
        new_node.parent = href_node.parent
        href_node.parent = None


def get_id_nodes(memory, node):
    """ If the node has an 'id' attribute, record it here. """

    node_id = node.attributes.get('id', None)

    if node_id is not None:
        memory[node_id] = node


def get_href_nodes(memory, node):

    node_href = node.attributes.get('href', None)

    if node_href is not None:
        memory.append(node)
