=============================================================================
List Floating Ips -  OpenStack Compute API v2.1
=============================================================================

List Floating Ips
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#request>`__
`Response <GET_list_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-floating-ips-bulk

Lists all floating IPs.



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








Response
^^^^^^^^^^^^^^^^^^





**Example List Floating Ips: JSON request**


.. code::

    {
        "floating_ip_info": [
            {
                "address": "10.10.10.1",
                "instance_uuid": null,
                "fixed_ip": null,
                "interface": "eth0",
                "pool": "nova",
                "project_id": null
            },
            {
                "address": "10.10.10.2",
                "instance_uuid": null,
                "fixed_ip": null,
                "interface": "eth0",
                "pool": "nova",
                "project_id": null
            },
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
    

