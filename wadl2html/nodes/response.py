
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

        if doc is None:
            output_html = child_html
            title = ""
        else:
            output_html = doc.to_html()
            title = doc.attributes.get('title', '')

        arguments = {
            "doc": doc,
            "node": self,
            "node_name": self.name,
            "attributes": self.attributes,
            "child_html": child_html,
            "title": title
        }

        if 'xmlns' in self.attributes:
            chosen_template = self.default_template
        else:
            chosen_template = self.extended_template

        template = jinja2.Template(chosen_template)
        return template.render(**arguments)
