
Enable Host
===========

.. rest_method:: PUT /v2.1/{tenant_id}/os-hosts/{host_name}

Enables or puts a host in maintenance mode.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../enableHost.yaml

	- tenant_id: tenant_id
	- host_name: host_name








**Example Enable Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-update-maintenance-req.json
   :language: javascript



Response
^^^^^^^^





**Example Enable Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-update-maintenance-resp.json
   :language: javascript


