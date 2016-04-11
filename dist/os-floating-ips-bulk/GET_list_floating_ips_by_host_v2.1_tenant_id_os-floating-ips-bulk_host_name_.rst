
List Floating Ips By Host
=========================

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ips-bulk/{host_name}

Lists all floating IPs for a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listFloatingIpsByHost.yaml

	- tenant_id: tenant_id
	- host_name: host_name








Response
^^^^^^^^





**Example List Floating Ips By Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips-bulk/floating-ips-bulk-list-by-host-resp.json
   :language: javascript


