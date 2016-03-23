=============================================================================
Delete Property Definition -  OpenStack Image API v2
=============================================================================

Delete Property Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_property_definition_v2_metadefs_namespaces_namespace_id_objects_object_name_.rst#request>`__
`Response <DELETE_delete_property_definition_v2_metadefs_namespaces_namespace_id_objects_object_name_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/metadefs/namespaces/{namespace_id}/objects/{object_name}

Deletes an object definition from a namespace.

To delete a protected object from a namespace, you must first set the ``protected`` attribute to false (boolean) on the namespace and then perform the delete. If you try to delete a protected object, the call returns the ``403`` response code.

When you successfully delete an object from a namespace, the response is empty and and the response code is ``204``.



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
|{object_name}             |xsd:string               |The name of the object.  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




