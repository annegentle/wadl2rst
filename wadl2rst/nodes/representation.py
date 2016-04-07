
from wadl2rst.nodes.base import BaseNode


class RepresentationNode(BaseNode):

    def to_example(self):
        code_node = self.find_first("xsdxt:sample")
        if code_node is None:
            return None

        char_node = code_node.find_first("char")
        if char_node is None:
            return None

        try:
            doc_node = self.find_one_of(["wadl:doc", "doc"])
            title = doc_node.attributes.get("title", None)
        except ValueError, e:
            title = None

        code_text = char_node.attributes['text']

        media_type = self.attributes.get('mediaType', None)
        media_type = mimetype_translation.get(media_type, "JSON")

        # TODO(auggy): modify the last word to match the samples in the nova repo

        return {
            "title": title,
            "type": media_type,
            "code": code_text
        }


mimetype_translation = {
    "application/json": "JSON",
    "application/xml": "XML"
}
