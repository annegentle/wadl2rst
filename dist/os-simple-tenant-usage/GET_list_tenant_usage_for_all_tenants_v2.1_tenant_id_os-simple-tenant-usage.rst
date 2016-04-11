
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







Response
^^^^^^^^





**Example List Tenant Usage For All Tenants: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-simple-tenant-usage/simple-tenant-usage-show-general-resp.json
   :language: javascript

