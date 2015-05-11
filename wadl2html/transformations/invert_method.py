import functools


def invert_method(tree):
    """ Given a tree, invert any resource -> method relationship to method ->
    resource. """

    resources_node = tree.find_first("resources")
    method_nodes = []

    for node in resources_node.children:
        if node.name != "resource":
            continue

        for child_node in node.children:
            if child_node.name != "method":
                continue

            new_node = node.clone()
            child_node.children.insert(1, new_node)
            method_nodes.append(child_node)

    for node in resources_node.children:
        node.children = [c for c in node.children if c.name != "method"]

    resources_node.children = method_nodes
