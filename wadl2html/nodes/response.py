
import jinja2

from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class ResponseNode(BaseNode):

    default_template = templates['response']
    extended_template = templates['response_extended']

    def to_html(self):
        doc = self.find_first("doc")

        # render all of the other children of this node
        child_html = ""

        for child in self.children:
            if child.name in ['doc']:
                continue

            child_html += child.to_html()

        arguments = {
            "doc": doc,
            "doc_html": doc.to_html(),
            "node": self,
            "node_name": self.name,
            "attributes": self.attributes,
            "child_html": child_html
        }

        if 'xmlns' in self.attributes:
            chosen_template = self.default_template
        else:
            chosen_template = self.extended_template

        template = jinja2.Template(chosen_template)
        return template.render(**arguments)
