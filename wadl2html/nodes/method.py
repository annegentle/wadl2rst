
import jinja2
import re

from wadl2html.nodes.base import BaseNode
from wadl2html.templates import templates


class MethodNode(BaseNode):
    template = templates['method']
    doc_names = ["wadl:doc", "doc"]
    para_names = ["para", "p", "db:para", "xhtml:p"]

    def get_filename(self):
        args = self.get_template_arguments()

        title = args['title'].strip().lower()
        title = re.sub(ur" ", "_", title)

        full_path = args['full_path'].strip().lower()
        full_path = re.sub(ur"/", "_", full_path)
        full_path = re.sub(ur"{", "", full_path)
        full_path = re.sub(ur"}", "", full_path)

        http_method = args['http_method'].strip()

        output = "{}_{}_{}.rst".format(http_method, title, full_path)
        output = re.sub(ur"__", "_", output)
        return output

    def to_rst(self):
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
        method_id = self.attributes.get("id", "")

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
            "child_rst": "",
            "docs_rst": "",
            "full_path": "",
            "method_id": method_id,
            "method_name": "",
            "params_rst": "",
            "title": ""
        }

        if docs is not None:
            output["docs_rst"] = docs.to_rst()

            if "title" in docs.attributes:
                output["title"] = docs.attributes['title']

        if short_desc is not None:
            output["desc_rst"] = short_desc.to_rst()

        if "name" in self.attributes:
            output["http_method"] = self.attributes['name']

        if (resource is not None) and ("full_path" in resource.attributes):
            output["full_path"] = resource.attributes['full_path']

        for child in self.children:
            # skip these, we're placing them manually
            if child in [docs, resource, params]:
                continue

            output['child_rst'] += child.to_rst()

        return output
