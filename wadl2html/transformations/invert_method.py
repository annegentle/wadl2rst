
import functools


def invert_method(tree):
    """ Given a tree, invert any resource -> method relationship to method ->
    resource. """

    resources_node = tree.find_first("resources")
    method_nodes = []

    # for each resource, flip it with any methods contained within
    for node in resources_node.children:
        if node.name != "resource":
            continue

        for child_node in node.children:
            if child_node.name != "method":
                continue

            new_node = node.clone()
            child_node.children.insert(1, new_node)
            method_nodes.append(child_node)

    resources_node.children = method_nodes

    # make sure no existing resource nodes have methods as children
    resource_nodes = []
    resource_visitor = functools.partial(get_resource_nodes, resource_nodes)
    tree.visit(resource_visitor)

    for node in resource_nodes:
        node.children = [c for c in node.children if c.name != "method"]


def get_resource_nodes(memory, node):
    if node.name == "resource":
        memory.append(node)
