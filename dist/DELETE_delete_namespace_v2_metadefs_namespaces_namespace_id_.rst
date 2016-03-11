=============================================================================
Delete Namespace -  OpenStack Compute API v2.1
=============================================================================

Delete Namespace
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_namespace_v2_metadefs_namespaces_namespace_id_.rst#request>`__
`Response <DELETE_delete_namespace_v2_metadefs_namespaces_namespace_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/metadefs/namespaces/{namespace_id}

Deletes a namespace and its properties, objects, and any resource type associations.

You cannot delete namespaces with the ``protected`` attribute set to ``true`` (boolean); the response returns the HTTP ``403`` response code.

To delete a namespace, you must first make an update namespace request to set the ``protected`` attribute to false (boolean) on the namespace. Then, delete the namespace.

A successful operation returns the HTTP ``204`` response code.

If you try to remove a namespace with the ``protected`` attribute set to true (boolean), the operation fails and the response returns the HTTP ``403`` response code.



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








Response
^^^^^^^^^^^^^^^^^^




