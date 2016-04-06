
List Tenant Usage For All Tenants
=================================

`Request <GET_list_tenant_usage_for_all_tenants_v2.1_tenant_id_os-simple-tenant-usage.rst#request>`__
`Response <GET_list_tenant_usage_for_all_tenants_v2.1_tenant_id_os-simple-tenant-usage.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-simple-tenant-usage

Lists usage information for all tenants.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





**Example List Tenant Usage For All Tenants: JSON request**


.. code::

    {
        "tenant_usages": [
            {
                "start": "2012-10-08T21:10:44.587336",
                "stop": "2012-10-08T22:10:44.587336",
                "tenant_id": "openstack",
                "total_hours": 1.0,
                "total_local_gb_usage": 1.0,
                "total_memory_mb_usage": 512.0,
                "total_vcpus_usage": 1.0
            }
        ]
    }
    

