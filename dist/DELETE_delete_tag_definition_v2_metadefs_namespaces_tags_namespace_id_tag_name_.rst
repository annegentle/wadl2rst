=============================================================================
Delete Tag Definition -  OpenStack Compute API v2.1
=============================================================================

Delete Tag Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#request>`__
`Response <DELETE_delete_tag_definition_v2_metadefs_namespaces_tags_namespace_id_tag_name_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/metadefs/namespaces/tags/{namespace_id}/{tag_name}

Deletes a tag definition within a namespace.

You cannot delete tags in a namespace with the 'protected' attribute set to true (boolean); the response returns the HTTP 403 status code.

You must first set the ``protected`` attribute to false (boolean) on the namespace and then perform the delete. The response is empty and returns the HTTP 204 status code.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tag_name}                |xsd:string               |The name of the tag.     |
+--------------------------+-------------------------+-------------------------+
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




