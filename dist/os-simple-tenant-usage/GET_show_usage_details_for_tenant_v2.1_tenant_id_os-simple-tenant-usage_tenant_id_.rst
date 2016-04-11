
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


.. literalinclude:: ../../../doc/api_samples/os-simple-tenant-usage/simple-tenant-usage-show-resp.json
   :language: javascript

