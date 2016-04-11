
List Floating Ips By Host
=========================

`Request <GET_list_floating_ips_by_host_v2.1_tenant_id_os-floating-ips-bulk_host_name_.rst#request>`__
`Response <GET_list_floating_ips_by_host_v2.1_tenant_id_os-floating-ips-bulk_host_name_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ips-bulk/{host_name}

Lists all floating IPs for a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Floating Ips By Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips-bulk/floating-ips-bulk-list-by-host-resp.json
   :language: javascript

