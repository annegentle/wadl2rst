
Bulk-Delete Floating Ips
========================

`Request <POST_bulk-delete_floating_ips_v2.1_tenant_id_os-floating-ips-bulk_delete.rst#request>`__
`Response <POST_bulk-delete_floating_ips_v2.1_tenant_id_os-floating-ips-bulk_delete.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-floating-ips-bulk/delete

Bulk-deletes floating IPs.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../bulk-deleteFloatingIps.yaml

	- ip_range: ip_range




**Example Bulk-Delete Floating Ips: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips-bulk/floating-ips-bulk-delete-req.json
   :language: javascript



Response
^^^^^^^^





**Example Bulk-Delete Floating Ips: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips-bulk/floating-ips-bulk-delete-resp.json
   :language: javascript

