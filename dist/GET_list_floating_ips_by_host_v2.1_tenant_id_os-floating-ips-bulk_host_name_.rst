=============================================================================
List Floating Ips By Host -  OpenStack Compute API v2.1
=============================================================================

List Floating Ips By Host
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_floating_ips_by_host_v2.1_tenant_id_os-floating-ips-bulk_host_name_.rst#request>`__
`Response <GET_list_floating_ips_by_host_v2.1_tenant_id_os-floating-ips-bulk_host_name_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-floating-ips-bulk/{host_name}

Lists all floating IPs for a host.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{host_name}               |xsd:string               |The name of the host.    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Floating Ips By Host: JSON request**


.. code::

    {
        "floating_ip_info": [
            {
                "address": "10.10.10.3",
                "instance_uuid": null,
                "fixed_ip": null,
                "interface": "eth0",
                "pool": "nova",
                "project_id": null
            }
        ]
    }
    

