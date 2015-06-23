
import jinja2

from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class MethodNode(BaseNode):
    template = templates['method']
    document_node_names = ["wadl:doc", "doc"]
    para_names = ["para", "p", "db:para", "xhtml:p"]

    def to_rst(self):
        """ Return the html representation of this tag and it's children. """

        child_rst = " ".join([child.to_rst() for child in self.children])

        template = jinja2.Template(self.template)
        return template.render(**self.template_params())

    def template_params(self):
        method_id = self.attributes.get("id", "")

        try:
            document_node = self.find_one_of(self.document_node_names)
            short_desc_node = document_node.find_one_of(self.para_names)
            resource_node = self.find_first("resource")
            responses_node = self.find_first("responses")
        except Exception:
            # we handle failures here below
            pass

        output = {
            "docs_rst": "",
            "filename": "find me",
            "http_method": self.attributes.get("name", None),
            "responses": [],
            "short_desc": "",
            "title": "",
            "uri": "",
        }

        # handle document node information
        if document_node is not None:
            output["docs_rst"] = document_node.to_rst()
            output["title"] = document_node.attributes.get("title", None)

        # handle resource node information
        if resource_node is not None:
            output["uri"] = resource_node.attributes.get("full_path", None)

        # handle short description information
        if short_desc_node is not None:
            output["short_desc"] = short_desc_node.to_rst()

        # handle responses nodes
        if responses_node is not None:
            for child in responses_node.children:
                output["responses"].append(self.get_response_info(child))

        return output

    def get_response_info(self, node):
        doc_node = node.find_one_of(self.document_node_names)

        return {
            "code": node.attributes['status'],
            "name": doc_node.attributes['title'],
            "desc": doc_node.to_rst()
        }
