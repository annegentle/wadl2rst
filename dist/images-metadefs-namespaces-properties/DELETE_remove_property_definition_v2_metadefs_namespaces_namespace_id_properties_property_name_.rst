=============================================================================
Remove Property Definition -  OpenStack Image API v2
=============================================================================

Remove Property Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_remove_property_definition_v2_metadefs_namespaces_namespace_id_properties_property_name_.rst#request>`__
`Response <DELETE_remove_property_definition_v2_metadefs_namespaces_namespace_id_properties_property_name_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/metadefs/namespaces/{namespace_id}/properties/{property_name}

Removes a property definition in a namespace.

To remove a property, first make an update namespace request to set the ``protected`` attribute to false (boolean) on the namespace. Then, remove the property. If the operation succeeds, the response returns the HTTP 204 status code.

If you try to remove a property in a namespace with the ``protected`` attribute set to true (boolean), the operation fails and the response returns the HTTP 403 error code.



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
|{property_name}           |xsd:string               |The name of the property.|
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|property_name             |xsd:string *(Required)*  |The name of the property.|
+--------------------------+-------------------------+-------------------------+





Response
^^^^^^^^^^^^^^^^^^




