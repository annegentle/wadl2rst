

def cleanup_application_node(tree):
    """ The only node that should be a child of the application node is the
    resources node. """

    children = []

    for child in tree.children:
        if child.name != "resources":
            child.parent = None
        else:
            children.append(child)

    tree.children = children
