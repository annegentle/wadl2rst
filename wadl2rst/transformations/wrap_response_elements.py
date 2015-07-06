
import functools

from wadl2rst.nodes.responses import ResponsesNode


def wrap_response_elements(tree):
    """ Find all the <response> nodes and make sure they are wrapped by <responses>
    nodes. """

    # grab all the response nodes
    response_nodes = []
    response_vistor = functools.partial(get_response_nodes, response_nodes)
    tree.visit(response_vistor)

    for node in response_nodes:
        parent = node.parent
        responses_node = None

        if node.parent.name == "responses":
            continue

        # try to find a responses node on the parent
        for sibling in parent.children:
            if sibling.name == "responses":
                responses_node = sibling
                break

        # no responses node, so add one
        if responses_node is None:
            responses_node = ResponsesNode(parent, "responses", {})
            parent.add_child(responses_node)

        # now move the node under the responses node
        node.parent = responses_node
        responses_node.add_child(node)
        parent.remove_child(node)


def get_response_nodes(memory, node):
    if node.name == "response" and node.parent.name != "responses":
        memory.append(node)
