
import functools


def resolve_internal(tree):
    """ Given a tree, replace any nodes with an 'href' attribute
    with the node with a corresponding 'id'. """

    # get all the nodes with an id attribute
    id_map = {}
    id_visitor = functools.partial(get_nodes_with_attribute, id_map, 'id')
    tree.visit(id_visitor)

    # get all the nodes with an href attribute
    href_map = {}
    href_visitor = functools.partial(get_nodes_with_attribute, href_map, 'href')
    tree.visit(href_visitor)

    # replace each node in the href map with a node in the id map
    for key, href_node in href_map.items():
        key = key.strip("#")

        # grab the id node associated with the href node
        id_node = id_map.get(key, None)
        if id_node is None:
            continue

        # since this node is used by-reference, we'll remove it from where it's defined
        if id_node.parent is not None:
            id_node.parent.remove_child(id_node)
            id_node.parent = None

        # replace the href_node with the id_node
        href_node.parent.replace_child(href_node, id_node)
        id_node.parent = href_node.parent
        href_node.parent = None


def get_nodes_with_attribute(memory, attribute, node):
    """ If the node has an 'id' attribute, record it here. """

    node_attribute = node.attributes.get(attribute, None)

    if node_attribute is not None:
        memory[node_attribute] = node
