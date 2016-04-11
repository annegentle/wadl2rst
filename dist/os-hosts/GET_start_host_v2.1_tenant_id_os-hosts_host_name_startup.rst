
Start Host
==========

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/startup

Starts a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../startHost.yaml

	- tenant_id: tenant_id
	- host_name: host_name








Response
^^^^^^^^





**Example Start Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-start-resp.json
   :language: javascript


