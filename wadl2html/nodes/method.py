
import jinja2

from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class MethodNode(BaseNode):
    template = templates['method']

    def to_html(self):
        docs = self.find_first("wadl:doc")

        # if the docs arent a <wadl:doc> try a plain <doc>
        if docs is None:
            docs = self.find_first("doc")

        short_desc = docs.find_first("para")

        # if the first paragraph isn't a <para> tag, try a <p> tag
        if short_desc is None:
            short_desc = self.find_first("p")

        resource = self.find_first("resource")
        params = resource.find_first("params")

        if params is not None:
            params_html = params.to_html()
        else:
            params_html = ""

        # render all of the other children of this node
        child_html = ""
        for child in self.children:
            # skip these, we're placing them manually
            if child in [docs, resource, params]:
                continue

            child_html += child.to_html()

        arguments = {
            "node": self,
            "node_name": self.name,
            "attributes": self.attributes,
            "child_html": child_html,
            "docs": docs,
            "docs_html": docs.to_html(),
            "resource": resource,
            "params_html": params_html,
            "short_desc": short_desc.to_html()
        }

        template = jinja2.Template(self.template)
        return template.render(**arguments)
