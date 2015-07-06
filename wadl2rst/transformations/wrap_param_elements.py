
import functools

from wadl2rst.nodes.parameters import ParametersNode


def wrap_param_elements(tree):
    """ Find all the <param> nodes and make sure they are wrapped by <params>
    nodes. """

    # grab all the param nodes
    param_nodes = []
    param_vistor = functools.partial(get_param_nodes, param_nodes)
    tree.visit(param_vistor)

    for node in param_nodes:
        parent = node.parent
        params_node = None

        if node.parent.name == "params":
            continue

        # try to find a params node on the parent
        for sibling in parent.children:
            if sibling.name == "params":
                params_node = sibling
                break

        # no params node, so add one
        if params_node is None:
            params_node = ParametersNode(parent, "params", {})
            parent.add_child(params_node)

        # now move the node under the params node
        node.parent = params_node
        params_node.add_child(node)
        parent.remove_child(node)


def get_param_nodes(memory, node):
    if node.name == "param" and node.parent.name != "params":
        memory.append(node)
