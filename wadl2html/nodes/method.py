
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

        template = jinja2.Template(self.template)
        return template.render(**self.get_template_arguments())

    def get_template_arguments(self):
        """ Get the arguments for the jinja2 template.  Since the wadls vary so
        widly, this is written to be super defensive. """

        resource = None
        params = None
        docs = None
        short_desc = None

        try:
            resource = self.find_first("resource")
            params = resource.find_first("params")
            docs = self.find_one_of(self.doc_names)
            short_desc = docs.find_one_of(self.para_names)
        except Exception:
            # we handle failures here below
            pass

        # defaults for the output
        output = {
            "method_name": "",
            "full_path": "",
            "title": "",
            "docs_html": "",
            "params_html": "",
            "child_html": ""
        }

        if docs is not None:
            output["docs_html"] = docs.to_html()

            if "title" in docs.attributes:
                output["title"] = docs.attributes['title']

        if short_desc is not None:
            output["desc_html"] = short_desc.to_html()

        if "name" in self.attributes:
            output["method_name"] = self.attributes['name']

        if (resource is not None) and ("full_path" in resource.attributes):
            output["full_path"] = resource.attributes['full_path']

        for child in self.children:
            # skip these, we're placing them manually
            if child in [docs, resource, params]:
                continue

            output['child_html'] += child.to_html()

        return output
