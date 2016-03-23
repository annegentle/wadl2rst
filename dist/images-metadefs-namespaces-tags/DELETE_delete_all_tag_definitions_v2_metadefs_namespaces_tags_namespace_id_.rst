=============================================================================
Delete All Tag Definitions -  OpenStack Image API v2
=============================================================================

Delete All Tag Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_all_tag_definitions_v2_metadefs_namespaces_tags_namespace_id_.rst#request>`__
`Response <DELETE_delete_all_tag_definitions_v2_metadefs_namespaces_tags_namespace_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/metadefs/namespaces/tags/{namespace_id}

Deletes all tag definitions within a namespace.

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
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|namespace                 |xsd:string *(Required)*  |The namespace is unique  |
|                          |                         |across all users.        |
+--------------------------+-------------------------+-------------------------+





Response
^^^^^^^^^^^^^^^^^^




