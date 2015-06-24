
import jinja2

from wadl2html import table
from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class MethodNode(BaseNode):
    template = templates['method']
    document_node_names = ["wadl:doc", "doc"]
    para_names = ["para", "p", "db:para", "xhtml:p"]

    def to_rst(self):
        """ Return the html representation of this tag and it's children. """

        child_rst = " ".join([child.to_rst() for child in self.children])
        return self.template.render(**self.template_params())

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
            "docs_rst": document_node.to_rst(),
            "filename": "find me",
            "http_method": self.attributes.get("name", None),
            "responses_table": "",
            "method_table": "",
            "short_desc": short_desc_node.to_rst(),
            "title": document_node.attributes.get("title", None),
            "uri": resource_node.attributes.get("full_path", None),
        }

        # handle the method table
        output['method_table'] = self.get_method_table(output)

        # handle responses nodes
        responses = [self.get_response_info(child) for child in responses_node.children]
        output['responses_table'] = self.get_responses_table(responses)

        return output

    def get_method_table(self, data):
        columns = ["Method", "URI", "Description"]
        http_method = "**{}**".format(data['http_method'])
        uri = "``{}``".format(data['uri'])
        desc = data['short_desc']
        return table.create_table(columns, [[http_method, uri, desc]])

    def get_responses_table(self, responses):
        columns = ["Response Code", "Name", "Description"]
        return table.create_table(columns, responses)

    def get_response_info(self, node):
        doc_node = node.find_one_of(self.document_node_names)

        return [
            node.attributes['status'],
            doc_node.attributes['title'],
            doc_node.to_rst()
        ]
