
import functools

from wadl2rst.nodes.base import BaseNode
from wadl2rst.nodes.parameters import ParametersNode


def collapse_resources(tree):
    """ In the input wadl, the resource uris are split out into a nested
    structure with each resource slug having it's own level.  For the output,
    we only care about the methods that can be done on resources. """

    # grab all the resources nodes with method nodes under them.
    resource_nodes = []
    resource_visitor = functools.partial(get_resource_nodes, resource_nodes)
    tree.visit(resource_visitor)

    # get resource types and add methods to resource nodes
    resource_type_nodes = []
    resource_type_visitor = functools.partial(get_resource_type_nodes, resource_type_nodes)
    tree.visit(resource_type_visitor)

    # get resource types and add methods to resource nodes
    # append method nodes to the appropriate resource node
    for rtnode in resource_type_nodes:

        # remove the resource_type node from the tree
        #  this prevents an id conflict down the line
        rtnode.parent.remove_child(rtnode)

        # extract method node
        for child in rtnode.children:

            if child.name == "method":
                method_node = child

                # look up resource node
                #  this is really inefficient but I can't figure out how to get the node while keeping it in scope
                for rnode in resource_nodes:
                    type_name = '#' + rtnode.attributes['id']
                    found_node = find_resource_nodes_with_type(type_name, rnode)
                    if not found_node:
                        for rn in rnode.children:
                            found_node = find_resource_nodes_with_type(type_name, rn)
                            if found_node:
                                break

                    if not found_node:
                        continue

                    # change the parent of the method node to the resource node
                    method_node.parent = found_node
                    # add the method node to the resource node's children
                    found_node.add_child(method_node)

    # setup the path for each node properly
    for node in resource_nodes:
        setup_node_path(node)

    # remove each node from the tree
    for node in reversed(resource_nodes):
        node.parent.remove_child(node)
        node.parent = None

    resources_node = tree.find_first("resources")

    # if there is no <resources> node on the page, add one.
    if resources_node is None:
        resources_node = BaseNode(tree, "resources", {})
        tree.add_child(resources_node)

    resources_node.children = []

    # setup the resources nodes in their proper place
    for node in resource_nodes:
        resources_node.add_child(node)
        node.parent = resources_node

    # remove any param nodes not nested in params
    param_nodes = []
    param_visitor = functools.partial(get_param_nodes, param_nodes)
    tree.visit(param_visitor)

    for node in set(param_nodes):
        node.parent.remove_child(node)
        node.parent = None

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
        if 'path' in current.attributes:
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

    if len(params) > 0:
        params_node = ParametersNode(node, 'params', {})
        node.children.insert(0, params_node)

        for param in params:
            clone = param.clone()
            params_node.add_child(clone)
            clone.parent = params_node


def get_param_nodes(memory, node):
    if (node.name == "param") and (node.parent.name == "resource"):
        memory.append(node)


def get_empty_resource_nodes(memory, node):
    child_names = [child.name for child in node.children]

    if (node.name == "resource") and ("method" not in child_names):
        memory.append(node)


def get_resource_nodes(memory, node):
    child_names = [child.name for child in node.children]

    if (node.name == "resource") and ("method" in child_names):
        memory.append(node)


def get_resource_type_nodes(memory, node):
    child_names = [child.name for child in node.children]

    if (node.name == "resource_type") and ("method" in child_names):
        memory.append(node)

def find_resource_nodes_with_type(type_name, node):
    if ("type" in node.attributes) and (node.attributes['type'] == type_name):
        return node