=============================================================================
Create Object -  OpenStack Image API v2
=============================================================================

Create Object
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_object_v2_metadefs_namespaces_namespace_id_objects.rst#request>`__
`Response <POST_create_object_v2_metadefs_namespaces_namespace_id_objects.rst#response>`__

.. code-block:: javascript

    POST /v2/metadefs/namespaces/{namespace_id}/objects

Creates an object definition in a namespace.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
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

+---------------------------+-------------------------+------------------------+
|Name                       |Type                     |Description             |
+===========================+=========================+========================+
|namespace                  |xsd:string *(Required)*  |The namespace is unique |
|                           |                         |across all users.       |
+---------------------------+-------------------------+------------------------+
|display_name               |xsd:string *(Required)*  |User-friendly name to   |
|                           |                         |use in a UI to display  |
|                           |                         |the namespace name.     |
+---------------------------+-------------------------+------------------------+
|description                |xsd:string *(Required)*  |Detailed description    |
|                           |                         |for the namespace.      |
+---------------------------+-------------------------+------------------------+
|visibility                 |xsd:string *(Required)*  |Namespace visibility.   |
|                           |                         |Valid value is          |
|                           |                         |``public`` or           |
|                           |                         |``private``. Default is |
|                           |                         |``private``.            |
+---------------------------+-------------------------+------------------------+
|protected                  |xsd:boolean *(Required)* |Namespace protection    |
|                           |                         |for deletion. Valid     |
|                           |                         |value is ``true`` or    |
|                           |                         |``false``. Default is   |
|                           |                         |``false``.              |
+---------------------------+-------------------------+------------------------+
|properties                 |xsd:dict *(Required)*    |Namespace property      |
|                           |                         |definitions, if any.    |
+---------------------------+-------------------------+------------------------+
|objects                    |xsd:dict *(Required)*    |Namespace object        |
|                           |                         |definitions, if any.    |
+---------------------------+-------------------------+------------------------+
|resource_type_associations |xsd:dict *(Required)*    |Namespace resource      |
|                           |                         |types, if any.          |
+---------------------------+-------------------------+------------------------+





**Example Create Object: JSON request**


.. code::

    {
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
        "required": []
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+---------------------------+-------------------------+------------------------+
|Name                       |Type                     |Description             |
+===========================+=========================+========================+
|namespace                  |xsd:string *(Required)*  |The namespace is unique |
|                           |                         |across all users.       |
+---------------------------+-------------------------+------------------------+
|display_name               |xsd:string *(Required)*  |User-friendly name to   |
|                           |                         |use in a UI to display  |
|                           |                         |the namespace name.     |
+---------------------------+-------------------------+------------------------+
|description                |xsd:string *(Required)*  |The description of the  |
|                           |                         |namespace.              |
+---------------------------+-------------------------+------------------------+
|visibility                 |xsd:string *(Required)*  |The namespace           |
|                           |                         |visibility. A valid     |
|                           |                         |value is ``public`` or  |
|                           |                         |``private``. Default is |
|                           |                         |``private``.            |
+---------------------------+-------------------------+------------------------+
|protected                  |xsd:string *(Required)*  |Namespace protection    |
|                           |                         |for deletion. A valid   |
|                           |                         |value is ``True`` or    |
|                           |                         |``False``. Default is   |
|                           |                         |``False``.              |
+---------------------------+-------------------------+------------------------+
|properties                 |xsd:dict *(Required)*    |One or more property    |
|                           |                         |definitions for the     |
|                           |                         |namespace.              |
+---------------------------+-------------------------+------------------------+
|objects                    |xsd:string *(Required)*  |One or more object      |
|                           |                         |definitions of the      |
|                           |                         |namespace.              |
+---------------------------+-------------------------+------------------------+
|resource_type_associations |xsd:string *(Required)*  |One or more namespace   |
|                           |                         |resource types.         |
+---------------------------+-------------------------+------------------------+





**Example Create Object: JSON request**


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
    

