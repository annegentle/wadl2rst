=============================================================================
Update Object Definition -  OpenStack Image API v2
=============================================================================

Update Object Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_object_definition_v2_metadefs_namespaces_namespace_id_objects_object_name_.rst#request>`__
`Response <PUT_update_object_definition_v2_metadefs_namespaces_namespace_id_objects_object_name_.rst#response>`__

.. code-block:: javascript

    PUT /v2/metadefs/namespaces/{namespace_id}/objects/{object_name}

Updates an object definition in a namespace.



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
|{object_name}             |xsd:string               |The name of the object.  |
+--------------------------+-------------------------+-------------------------+








**Example Update Object Definition: JSON request**


.. code::

    {
        "description": "You can configure the CPU limits with control parameters.",
        "name": "CPU Limits",
        "properties": {
            "quota:cpu_shares": {
                "description": "Specifies the proportional weighted share for the domain. If this element is omitted, the service defaults to the OS provided defaults. There is no unit for the value; it is a relative measure based on the setting of other VMs. For example, a VM configured with value 2048 gets twice as much CPU time as a VM configured with value 1024.",
                "title": "Quota: CPU Shares",
                "type": "integer"
            }
        },
        "required": []
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Update Object Definition: JSON request**


.. code::

    {
        "created_at": "2014-09-19T19:20:56Z",
        "description": "You can configure the CPU limits with control parameters.",
        "name": "CPU Limits",
        "properties": {
            "quota:cpu_shares": {
                "description": "Specifies the proportional weighted share for the domain. If this element is omitted, the service defaults to the OS provided defaults. There is no unit for the value; it is a relative measure based on the setting of other VMs. For example, a VM configured with value 2048 gets twice as much CPU time as a VM configured with value 1024.",
                "title": "Quota: CPU Shares",
                "type": "integer"
            }
        },
        "required": [],
        "schema": "/v2/schemas/metadefs/object",
        "self": "/v2/metadefs/namespaces/OS::Compute::Quota/objects/CPU Limits",
        "updated_at": "2014-09-19T19:20:56Z"
    }
    

