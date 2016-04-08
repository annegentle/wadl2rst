
Show Usage Details For Tenant
=============================

`Request <GET_show_usage_details_for_tenant_v2.1_tenant_id_os-simple-tenant-usage_tenant_id_.rst#request>`__
`Response <GET_show_usage_details_for_tenant_v2.1_tenant_id_os-simple-tenant-usage_tenant_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-simple-tenant-usage/{tenant_id}

Shows usage details for a tenant.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





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
    

