
List Floating Ips
=================

`Request <GET_list_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#request>`__
`Response <GET_list_floating_ips_v2.1_tenant_id_os-floating-ips-bulk.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ips-bulk

Lists all floating IPs.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Floating Ips: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips-bulk/floating-ips-bulk-list-resp.json
   :language: javascript

