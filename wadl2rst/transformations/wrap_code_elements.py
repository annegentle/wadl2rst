
from wadl2rst.nodes.base import BaseNode


def wrap_code_elements(tree):
    """ Find all the <xsdxt:code> nodes and make sure they are wrapped by <xsdxt:sample>
    nodes. """

    # grab all the param nodes
    code_nodes = tree.find("xsdxt:code")

    for node in code_nodes:
        parent = node.parent
        sample_node = None

        if node.parent.name == "xsdxt:sample":
            continue

        # try to find a xsdxt:sample node on the parent
        for sibling in parent.children:
            if sibling.name == "xsdxt:sample":
                sample_node = sibling
                break

        # no xsdxt:sample node, so add one
        if sample_node is None:
            sample_node = BaseNode(parent, "xsdxt:sample", {})
            parent.add_child(sample_node)

        # now move the node under the params node
        node.parent = sample_node
        sample_node.add_child(node)
        parent.remove_child(node)
