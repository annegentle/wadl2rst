=============================================================================
Add Tag Definition -  OpenStack Image API v2
=============================================================================

Add Tag Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_add_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#request>`__
`Response <POST_add_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#response>`__

.. code-block:: javascript

    POST /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Adds a tag to the list of namespace tag definitions.



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





**Example Add Tag Definition: JSON request**


.. code::

    {
        "created_at": "2015-05-09T01:12:31Z",
        "name": "added-sample-tag",
        "updated_at": "2015-05-09T01:12:31Z"
    }
    

