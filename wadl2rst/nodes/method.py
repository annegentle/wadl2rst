
import re

from wadl2rst import table
from wadl2rst.nodes.base import BaseNode
from wadl2rst.templates import templates


FILENAME_TITLE = re.compile(r" ")
FILENAME_PATH = re.compile(r"/|{|}")
FILENAME_UNDERSCORES = re.compile(r"[_]+")


class MethodNode(BaseNode):
    template = templates['method']
    document_node_names = ["wadl:doc", "doc"]
    para_names = ["para", "p", "db:para", "xrst:p"]

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        return self.template.render(**self.template_params())

    def template_params(self):
        try:
            document_node = self.find_one_of(self.document_node_names)
            short_desc_node = document_node.find_one_of(self.para_names)
            resource_node = self.find_first("resource")
            responses_node = self.find_first("responses")
            request_node = self.find_first("request")
        except Exception:
            # we handle failures here below
            pass

        output = {
            "body_table": None,
            "docs_rst": document_node.to_rst(),
            "filename": "",
            "http_method": self.attributes.get("name", ''),
            "method_table": None,
            "query_table": None,
            "request_examples": [],
            "responses_table": None,
            "response_examples": [],
            "short_desc": short_desc_node.to_rst(),
            "title": document_node.attributes.get("title", '').title(),
            "uri_table": None,
            "uri": resource_node.attributes.get("full_path", ''),
        }

        # setup the resource node stuff
        if resource_node is not None:
            uri_params = resource_node.find_first("params")
            if uri_params is not None:
                output['uri_table'] = uri_params.to_table()

        # setup some request node stuff
        if request_node is not None:
            request_params = request_node.find_first("params")

            if request_params is not None:
                output['query_table'] = request_params.to_table("query")
                output['body_table'] = request_params.to_table("plain")

            # stash any request examples
            representations = request_node.find("representation")
            for representation in representations:
                example = representation.to_example()
                if example is not None:
                    output['request_examples'].append(example)

        # setup the reponses node stuff
        if responses_node is not None:
            response_params = responses_node.find_first("params")

            # stash the responses table
            if response_params is not None:
                output['response_table'] = response_params.to_table("plain")

            # stash any response examples
            representations = responses_node.find("representation")
            for representation in representations:
                example = representation.to_example()
                if example is not None:
                    output['response_examples'].append(example)

        # handle the method table
        output['method_table'] = self.get_method_table(output)

        # handle responses nodes
        responses = [self.get_response_info(child) for child in responses_node.children]
        output['responses_table'] = self.get_responses_table(responses)

        # create the filename
        output['filename'] = self.get_filename(output, 'rst')

        return output

    def get_filename(self, data=None, extention="rst"):
        http_method = data['http_method']

        title = FILENAME_TITLE.sub("_", data['title'].lower())
        uri = FILENAME_PATH.sub("_", data['uri'].lower())

        output = "{}_{}_{}.{}".format(
            http_method,
            title,
            uri,
            extention
        )

        output = FILENAME_UNDERSCORES.sub("_", output)
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
        clone = node.clone()

        reps = [child for child in clone.children if child.name == "representation"]
        for rep in reps:
            clone.remove_child(rep)

        title = ""

        try:
            doc_node = node.find_one_of(self.document_node_names)
            title = doc_node.attributes.get('title', '')
        except ValueError, e:
            title = ""

        return [
            node.attributes['status'],
            title,
            clone.to_rst()
        ]
