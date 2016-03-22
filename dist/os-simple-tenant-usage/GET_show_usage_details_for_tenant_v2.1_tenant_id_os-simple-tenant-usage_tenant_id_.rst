=============================================================================
Show Usage Details For Tenant -  OpenStack Compute API v2.1
=============================================================================

Show Usage Details For Tenant
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_usage_details_for_tenant_v2.1_tenant_id_os-simple-tenant-usage_tenant_id_.rst#request>`__
`Response <GET_show_usage_details_for_tenant_v2.1_tenant_id_os-simple-tenant-usage_tenant_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-simple-tenant-usage/{tenant_id}

Shows usage details for a tenant.



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
|{tenant_id}               |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Usage Details For Tenant: JSON request**


.. code::

    {
        "tenant_usage": {
            "server_usages": [
                {
                    "ended_at": null,
                    "flavor": "m1.tiny",
                    "hours": 1.0,
                    "instance_id": "1f1deceb-17b5-4c04-84c7-e0d4499c8fe0",
                    "local_gb": 1,
                    "memory_mb": 512,
                    "name": "new-server-test",
                    "started_at": "2012-10-08T20:10:44.541277",
                    "state": "active",
                    "tenant_id": "openstack",
                    "uptime": 3600,
                    "vcpus": 1
                }
            ],
            "start": "2012-10-08T20:10:44.587336",
            "stop": "2012-10-08T21:10:44.587336",
            "tenant_id": "openstack",
            "total_hours": 1.0,
            "total_local_gb_usage": 1.0,
            "total_memory_mb_usage": 512.0,
            "total_vcpus_usage": 1.0
        }
    }
    

