
import jinja2

from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class MethodNode(BaseNode):
    template = templates['method']

    doc_names = ["wadl:doc", "doc"]
    para_names = ["para", "p", "db:para", "xhtml:p"]

    def to_html(self):
        # this was a link that could not be resolved, so don't show anything
        if "href" in self.attributes:
            return ""

        try:
            docs = self.find_one_of(self.doc_names)
            title = docs.attributes['title']
            docs_html = docs.to_html()
            short_desc = docs.find_one_of(self.para_names)
            desc_html = short_desc.to_html()
        except Exception, e:
            # issue with finding the description for this method
            desc_html = ""

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
            "docs_html": docs_html,
            "resource": resource,
            "params_html": params_html,
            "short_desc": desc_html
        }

        template = jinja2.Template(self.template)
        return template.render(**arguments)


def get_template_payload(node):
     method_name = node.attributes['name']
     path = ""
     title = ""
     docs = ""
     params = ""
     child = ""
