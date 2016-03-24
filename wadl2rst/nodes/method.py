
import re

from wadl2rst import table
from wadl2rst.nodes.base import BaseNode
from wadl2rst.templates import templates


FILENAME_TITLE = re.compile(r" |/")
FILENAME_PATH = re.compile(r"/|{|}")
FILENAME_UNDERSCORES = re.compile(r"[_]+")


class MethodNode(BaseNode):
    template = templates['method']
    document_node_names = ["wadl:doc", "doc"]
    para_names = ["para", "p", "db:para", "xhtml:p"]

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
            "body_table": None,
            "docs_rst": "",
            "filename": "",
            "http_method": self.attributes.get("name", ''),
            "query_table": None,
            "request_examples": [],
            "error_responses": None,
            "response_examples": [],
            "short_desc": "",
            "title": "",
            "uri_table": None,
            "uri": "",
        }

        if document_node is not None:
            output['docs_rst'] = document_node.to_rst()
            output['title'] = document_node.attributes.get("title", '').title()

        if short_desc_node is not None:
            output['short_desc'] = short_desc_node.to_rst()

        # setup the resource node stuff
        if resource_node is not None:
            output['uri'] = resource_node.attributes.get("full_path", '')
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

            # handle responses nodes
            responses = [self.get_response_info(child) for child in responses_node.children]
            if responses =
            output['responses_list'] = self.get_error_responses(responses)

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

    def get_error_responses(self, responses):
        # This should only contain errors, and a successful request should
        # be a single response HTTP code, but not sure how to return single
        responses_types_headings = ["Status Code", "Reason"]
        
        return table.create_table(responses_types_headings, responses)

    def get_response_info(self, node):
        clone = node.clone()

        reps = [child for child in clone.children if child.name == "representation"]
        for rep in reps:
            clone.remove_child(rep)

        faults = ""
        # How do you wrap at 79 chars when value string is long?
        computefaults = {
        'computeAPIFault': 'A generic Compute API fault.',
        'itemNotFoundAPIFault': 'The item or resource could not be found.'
        'buildInProgressAPIFault': 'The operation is not allowed because the '
                                   'corresponding server is in a build state.'
        'serverCapacityUnavailable': 'There is not enough capacity to honor '
                                    'the request.'
        'backupOrResizeInProgress': 'The operation is not allowed because the '
                                    'corresponding server is being re-sized '
                                    'or backed up.'
        'serviceUnavailable': 'The API service is currently unavailable.'
        'unauthorizedAPIFault': 'Insufficient privileges to honor the request. '
                                'Perhaps obtain or renew an authentication '
                                'token.'
        'forbiddenAPIFault': 'Authentication has been validated. However, '
                             'the operation is unauthorized.'
        'overLimitAPIFault': 'A rate limit has been exceeded.'
        'badRequest': 'The request is malformed.'
        'badMediaType': 'The Content Type of the request is not supported.'
        'badMethod': 'The HTTP method (or verb) is not supported by the '
                     'corresponding resource.'
        'notImplemented': 'The operation is currently not implemented.'
        }

        try:
            doc_node = node.find_one_of(self.document_node_names)
            faults = doc_node.attributes.get('element', '')
            # if the element matches one of the ones above, output that string
            
        except ValueError, e:
            faults = ""

        return [
            node.attributes.get('status', ''),
            faults,
            clone.to_rst()
        ]
