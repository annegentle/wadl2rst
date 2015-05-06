
import functools

from wadl2html.nodes.parameters import ParametersNode


def collapse_resources(tree):
    """ In the input wadl, the resource uris are split out into a nested
    structure with each resource slug having it's own level.  For the output,
    we only care about the methods that can be done on resources. """

    # grab all the resources nodes with method nodes under them.
    resource_nodes = []
    resource_visitor = functools.partial(get_resource_nodes, resource_nodes)
    tree.visit(resource_visitor)

    # setup the path for each node properly
    for node in resource_nodes:
        setup_node_path(node)

    # remove each node from the tree
    for node in reversed(resource_nodes):
        node.parent.remove_child(node)
        node.parent = None

    resources_node = tree.find_first("resources")
    resources_node.children = []

    # setup the resources nodes in their proper place
    for node in resource_nodes:
        resources_node.add_child(node)
        node.parent = resources_node

    # remove any resource nodes with no method children
    empty_resources = []
    empty_resource_visitor = functools.partial(get_empty_resource_nodes, empty_resources)
    tree.visit(empty_resource_visitor)

    for node in empty_resources:
        node.parent.remove_child(node)


def setup_node_path(node):
    """ Prep this node to exist outside it's hierarchy.  We'll need to give it
    it's full path, and make sure it has references to the path params. """

    current = node
    path = []
    params = []

    while current:
        # handle the path
        path.insert(0, current.attributes['path'].strip('/'))

        # grab any params that exist
        for child in current.children:
            if child.name == "param":
                params.insert(0, child)

        # if the current node has a parent that is a resource too, keep going
        if current.parent.name == "resource":
            current = current.parent
        else:
            current = None

    # setup the path for this node
    node.attributes['full_path'] = '/' + '/'.join(path)

    # if there are any path params, add them to the node also
    if len(params) > 0:
        params_node = ParametersNode(node, 'params', {})
        params_node.children = params
        node.children.insert(0, params_node)


def get_empty_resource_nodes(memory, node):
    child_names = [child.name for child in node.children]

    if (node.name == "resource") and ("method" not in child_names):
        memory.append(node)


def get_resource_nodes(memory, node):
    child_names = [child.name for child in node.children]

    if (node.name == "resource") and ("method" in child_names):
        memory.append(node)
