=============================================================================
Get Tag Definition -  OpenStack Image API v2
=============================================================================

Get Tag Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_get_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#request>`__
`Response <GET_get_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#response>`__

.. code-block:: javascript

    GET /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Gets a definition for a tag.

The response body shows a single tag entity.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+
|{tag_name}                |xsd:string               |The name of the tag.     |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The name of the tag.     |
+--------------------------+-------------------------+-------------------------+





**Example Get Tag Definition: JSON request**


.. code::

    {
        "created_at": "2015-05-06T23:16:12Z",
        "name": "sample-tag2",
        "updated_at": "2015-05-06T23:16:12Z"
    }
    

