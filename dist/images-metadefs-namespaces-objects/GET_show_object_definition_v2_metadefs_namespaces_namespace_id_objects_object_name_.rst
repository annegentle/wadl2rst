=============================================================================
Show Object Definition -  OpenStack Image API v2
=============================================================================

Show Object Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_object_definition_v2_metadefs_namespaces_namespace_id_objects_object_name_.rst#request>`__
`Response <GET_show_object_definition_v2_metadefs_namespaces_namespace_id_objects_object_name_.rst#response>`__

.. code-block:: javascript

    GET /v2/metadefs/namespaces/{namespace_id}/objects/{object_name}

Shows the definition for an object.

The response body shows a single object entity.



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








Response
^^^^^^^^^^^^^^^^^^





**Example Show Object Definition: JSON request**


.. code::

    {
        "created_at": "2014-09-19T18:20:56Z",
        "description": "You can configure the CPU limits with control parameters.",
        "name": "CPU Limits",
        "properties": {
            "quota:cpu_period": {
                "description": "Specifies the enforcement interval (unit: microseconds) for QEMU and LXC hypervisors. Within a period, each VCPU of the domain is not allowed to consume more than the quota worth of runtime. The value should be in range [1000, 1000000]. A period with value 0 means no value.",
                "maximum": 1000000,
                "minimum": 1000,
                "title": "Quota: CPU Period",
                "type": "integer"
            },
            "quota:cpu_quota": {
                "description": "Specifies the maximum allowed bandwidth (unit: microseconds). A domain with a negative-value quota indicates that the domain has infinite bandwidth, which means that it is not bandwidth controlled. The value should be in range [1000, 18446744073709551] or less than 0. A quota with value 0 means no value. You can use this feature to ensure that all vCPUs run at the same speed.",
                "title": "Quota: CPU Quota",
                "type": "integer"
            },
            "quota:cpu_shares": {
                "description": "Specifies the proportional weighted share for the domain. If this element is omitted, the service defaults to the OS provided defaults. There is no unit for the value; it is a relative measure based on the setting of other VMs. For example, a VM configured with value 2048 gets twice as much CPU time as a VM configured with value 1024.",
                "title": "Quota: CPU Shares",
                "type": "integer"
            }
        },
        "required": [],
        "schema": "/v2/schemas/metadefs/object",
        "self": "/v2/metadefs/namespaces/OS::Compute::Quota/objects/CPU Limits",
        "updated_at": "2014-09-19T18:20:56Z"
    }
    

