=============================================================================
List Object Definitions -  OpenStack Image API v2
=============================================================================

List Object Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_object_definitions_v2_metadefs_namespaces_namespace_id_objects.rst#request>`__
`Response <GET_list_object_definitions_v2_metadefs_namespaces_namespace_id_objects.rst#response>`__

.. code-block:: javascript

    GET /v2/metadefs/namespaces/{namespace_id}/objects

Lists object definitions in a namespace.

Returns a subset of the larger collection of namespaces and a link that you can use to get the next set of namespaces. You should always check for the presence of a ``next`` link and use it as the URI in a subsequent HTTP GET request. You should follow this pattern until a ``next`` link is no longer provided. The next link preserves any query parameters that you send in your initial request. You can use the ``first`` link to jump back to the first page of the collection. If you prefer to paginate through namespaces manually, use the ``limit`` and ``marker`` parameters.

Use the ``resource_types`` and ``visibility`` query parameters to filter the response.

For example, set the ``resource_types`` query parameter to ``OS::Glance::Image,OS::Nova::Flavor`` to filter the response to include only namespaces that are associated with the given resource types.

You can sort the results of this operation by using the ``sort_key`` and ``sort_dir`` parameters. The API uses the natural sorting of whatever namespace attribute is provided as the ``sort_key``.



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



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|visibility                |imageapi:string          |Filters the response by  |
|                          |*(Required)*             |a namespace visibility   |
|                          |                         |value. A valid value is  |
|                          |                         |``public`` or            |
|                          |                         |``private``. If you omit |
|                          |                         |this parameter, the      |
|                          |                         |response shows           |
|                          |                         |``public`` and           |
|                          |                         |``private`` namespaces.  |
+--------------------------+-------------------------+-------------------------+
|resource_types            |xsd:int *(Required)*     |Filters the response by  |
|                          |                         |a resource type or       |
|                          |                         |types. Use the comma (   |
|                          |                         |``,`` ) character to     |
|                          |                         |separate multiple        |
|                          |                         |values. For example,     |
|                          |                         |``OS::Glance::Image,     |
|                          |                         |OS::Nova::Flavor`` shows |
|                          |                         |only namespaces for      |
|                          |                         |these resource types.    |
+--------------------------+-------------------------+-------------------------+
|sort_key                  |xsd:string *(Required)*  |Sorts the response by an |
|                          |                         |attribute, such as       |
|                          |                         |``name``, ``id``, or     |
|                          |                         |``updated_at``. Default  |
|                          |                         |is ``created_at``. The   |
|                          |                         |API uses the natural     |
|                          |                         |sorting direction of the |
|                          |                         |``sort_key`` image       |
|                          |                         |attribute.               |
+--------------------------+-------------------------+-------------------------+
|sort_dir                  |xsd:string *(Required)*  |Sorts the response by a  |
|                          |                         |set of one or more sort  |
|                          |                         |direction and attribute  |
|                          |                         |( ``sort_key`` )         |
|                          |                         |combinations. A valid    |
|                          |                         |value for the sort       |
|                          |                         |direction is ``asc``     |
|                          |                         |(ascending) or ``desc``  |
|                          |                         |(descending). If you     |
|                          |                         |omit the sort direction  |
|                          |                         |in a set, the default is |
|                          |                         |``desc``.                |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+---------------------------+-------------------------+------------------------+
|Name                       |Type                     |Description             |
+===========================+=========================+========================+
|namespaces                 |xsd:list *(Required)*    |A list of ``namespace`` |
|                           |                         |objects.                |
+---------------------------+-------------------------+------------------------+
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
|resource_type_associations |xsd:string *(Required)*  |One or more namespace   |
|                           |                         |resource types.         |
+---------------------------+-------------------------+------------------------+





**Example List Object Definitions: JSON request**


.. code::

    {
        "objects": [
            {
                "created_at": "2014-09-18T18:16:35Z",
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
                "self": "/v2/metadefs/namespaces/OS::Compute::Quota/objects/CPU Limits"
            },
            {
                "created_at": "2014-09-18T18:16:35Z",
                "description": "Using disk I/O quotas, you can set maximum disk write to 10 MB per second for a VM user.",
                "name": "Disk QoS",
                "properties": {
                    "quota:disk_read_bytes_sec": {
                        "description": "Sets disk I/O quota for disk read bytes / sec.",
                        "title": "Quota: Disk read bytes / sec",
                        "type": "integer"
                    },
                    "quota:disk_read_iops_sec": {
                        "description": "Sets disk I/O quota for disk read IOPS / sec.",
                        "title": "Quota: Disk read IOPS / sec",
                        "type": "integer"
                    },
                    "quota:disk_total_bytes_sec": {
                        "description": "Sets disk I/O quota for total disk bytes / sec.",
                        "title": "Quota: Disk Total Bytes / sec",
                        "type": "integer"
                    },
                    "quota:disk_total_iops_sec": {
                        "description": "Sets disk I/O quota for disk total IOPS / sec.",
                        "title": "Quota: Disk Total IOPS / sec",
                        "type": "integer"
                    },
                    "quota:disk_write_bytes_sec": {
                        "description": "Sets disk I/O quota for disk write bytes / sec.",
                        "title": "Quota: Disk Write Bytes / sec",
                        "type": "integer"
                    },
                    "quota:disk_write_iops_sec": {
                        "description": "Sets disk I/O quota for disk write IOPS / sec.",
                        "title": "Quota: Disk Write IOPS / sec",
                        "type": "integer"
                    }
                },
                "required": [],
                "schema": "/v2/schemas/metadefs/object",
                "self": "/v2/metadefs/namespaces/OS::Compute::Quota/objects/Disk QoS"
            },
            {
                "created_at": "2014-09-18T18:16:35Z",
                "description": "Bandwidth QoS tuning for instance virtual interfaces (VIFs) may be specified with these properties. Incoming and outgoing traffic can be shaped independently. If not specified, no quality of service (QoS) is applied on that traffic direction. So, if you want to shape only the network's incoming traffic, use inbound only (and vice versa). The OpenStack Networking service abstracts the physical implementation of the network, allowing plugins to configure and manage physical resources. Virtual Interfaces (VIF) in the logical model are analogous to physical network interface cards (NICs). VIFs are typically owned a managed by an external service; for instance when OpenStack Networking is used for building OpenStack networks, VIFs would be created, owned, and managed in Nova. VIFs are connected to OpenStack Networking networks via ports. A port is analogous to a port on a network switch, and it has an administrative state. When a VIF is attached to a port the OpenStack Networking API creates an attachment object, which specifies the fact that a VIF with a given identifier is plugged into the port.",
                "name": "Virtual Interface QoS",
                "properties": {
                    "quota:vif_inbound_average": {
                        "description": "Network Virtual Interface (VIF) inbound average in kilobytes per second. Specifies average bit rate on the interface being shaped.",
                        "title": "Quota: VIF Inbound Average",
                        "type": "integer"
                    },
                    "quota:vif_inbound_burst": {
                        "description": "Network Virtual Interface (VIF) inbound burst in total kilobytes. Specifies the amount of bytes that can be burst at peak speed.",
                        "title": "Quota: VIF Inbound Burst",
                        "type": "integer"
                    },
                    "quota:vif_inbound_peak": {
                        "description": "Network Virtual Interface (VIF) inbound peak in kilobytes per second. Specifies maximum rate at which an interface can receive data.",
                        "title": "Quota: VIF Inbound Peak",
                        "type": "integer"
                    },
                    "quota:vif_outbound_average": {
                        "description": "Network Virtual Interface (VIF) outbound average in kilobytes per second. Specifies average bit rate on the interface being shaped.",
                        "title": "Quota: VIF Outbound Average",
                        "type": "integer"
                    },
                    "quota:vif_outbound_burst": {
                        "description": "Network Virtual Interface (VIF) outbound burst in total kilobytes. Specifies the amount of bytes that can be burst at peak speed.",
                        "title": "Quota: VIF Outbound Burst",
                        "type": "integer"
                    },
                    "quota:vif_outbound_peak": {
                        "description": "Network Virtual Interface (VIF) outbound peak in kilobytes per second. Specifies maximum rate at which an interface can send data.",
                        "title": "Quota: VIF Outbound Burst",
                        "type": "integer"
                    }
                },
                "required": [],
                "schema": "/v2/schemas/metadefs/object",
                "self": "/v2/metadefs/namespaces/OS::Compute::Quota/objects/Virtual Interface QoS"
            }
        ],
        "schema": "v2/schemas/metadefs/objects"
    }
    

