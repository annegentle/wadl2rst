
import re

from wadl2rst import table
from wadl2rst.nodes.base import BaseNode
from wadl2rst.templates import templates


FILENAME_TITLE = re.compile(r" |/")
FILENAME_PATH = re.compile(r"/|{|}")
FILENAME_UNDERSCORES = re.compile(r"[_]+")
PARAMS_YAML = re.compile(r"/s")
PARAMS_CLEANUP = re.compile(r"\(.*?\)")


class MethodNode(BaseNode):
    template = templates['method']
    document_node_names = ["wadl:doc", "doc"]
    para_names = ["para", "p", "db:para", "xhtml:p"]

    # TODO(auggy): should this take params as an argument?
    # self.template_params() is called twice, once here and
    # once after this returns to get the filename

    def to_rst(self, book_title):
        """ Return the rst representation of this tag and it's children. """

        # we were not able to resolve this method, so skip it
        if "href" in self.attributes:
            print "Unresolved method {}".format(self.attributes['href'])
            return ""

        params = self.template_params()

        try:
            return self.template.render(book_title=book_title, **params)
        except Exception, e:
            print params
            raise e

    def template_params(self):
        resource_node = None
        responses_node = None
        request_node = None
        document_node = None
        short_desc_node = None

        try:
            resource_node = self.find_first("resource")
        except Exception:
            pass

        try:
            responses_node = self.find_first("responses")
        except Exception:
            pass

        try:
            request_node = self.find_first("request")
        except Exception:
            pass

        try:
            document_node = self.find_one_of(self.document_node_names)
            short_desc_node = document_node.find_one_of(self.para_names)
        except Exception:
            # we handle failures here below
            pass


        output = {
            "body_table": u'',
            "docs_rst": "",
            "filename": "",
            "http_method": self.attributes.get("name", ''),
            "in_params": None,
            "params_yaml" : u'',
            "query_table": None,
            "request_examples": [],
            "responses_table": None,
            "response_examples": [],
            "short_desc": "",
            "title": "",
            "uri_table": u'',
            "uri": "",
        }

        if document_node is not None:
            output['docs_rst'] = document_node.to_rst()
            output['title'] = document_node.attributes.get("title", '').title()

        # create the params yaml filename
        params_yaml = PARAMS_CLEANUP.sub("", output['title'])
        params_yaml = PARAMS_YAML.sub("", params_yaml).split()
        params_yaml[0] = params_yaml[0].lower()
        output['params_yaml'] = ''.join(params_yaml) + '.yaml'

        if short_desc_node is not None:
            output['short_desc'] = short_desc_node.to_rst()

        # setup the resource node stuff
        if resource_node is not None:
            output['uri'] = resource_node.attributes.get("full_path", '')
            uri_params = resource_node.find_first("params")
            if uri_params is not None:
                output['uri_table'] = uri_params.to_keypairs()

        # setup some request node stuff
        if request_node is not None:
            request_params = request_node.find_first("params")

            if request_params is not None:
                output['query_table'] = request_params.to_keypairs("query")
                output['body_table'] = request_params.to_keypairs("plain")

            # stash any request examples
            representations = request_node.find("representation")
            for representation in representations:
                example = representation.to_example()
                if example is not None:
                    output['request_examples'].append(example)

        # set up in params
        output['in_params'] = output['uri_table'] + output['body_table']

        # setup the reponses node stuff
        if responses_node is not None:
            response_params = responses_node.find_first("params")

            # stash the responses table
            if response_params is not None:
                output['response_table'] = response_params.to_keypairs("plain")

            # handle responses nodes
            responses = [self.get_response_info(child) for child in responses_node.children]
            # output['responses_table'] = self.get_responses_table(responses)
            output['error_responses'] = self.get_error_responses_list(responses)
            output['normal_responses'] = self.get_normal_responses_list(responses)

            # stash any response examples
            representations = responses_node.find("representation")
            for representation in representations:
                example = representation.to_example()
                if example is not None:
                    output['response_examples'].append(example)

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

    def get_responses_table(self, responses):
        columns = ["Response Code", "Name", "Description"]
        return table.create_table(columns, responses)

    def get_error_responses_list(self, responses):
        # TODO(auggy): actually implement this, looks like it's not getting into the data
        return u'''computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)'''

    def get_normal_responses_list(self, responses):
        normal_responses = [i[0] for i in responses]
        return ','.join(normal_responses)

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
            node.attributes.get('status', ''),
            title,
            clone.to_rst()
        ]
