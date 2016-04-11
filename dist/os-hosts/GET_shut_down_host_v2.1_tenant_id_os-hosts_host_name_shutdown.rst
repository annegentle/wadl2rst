
Shut Down Host
==============

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/shutdown

Shuts down a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../shutDownHost.yaml

	- tenant_id: tenant_id
	- host_name: host_name








Response
^^^^^^^^





**Example Shut Down Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-shutdown-resp.json
   :language: javascript


