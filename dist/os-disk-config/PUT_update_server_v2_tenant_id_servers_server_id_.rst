
Update Server
=============

.. rest_method:: PUT /v2/{tenant_id}/servers/{server_id}

Updates a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../updateServer.yaml

	- tenant_id: tenant_id
	- os-disk-config:diskConfig: os-disk-config:diskConfig
	- server_id: server_id








**Example Update Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/server-update-put-req.json
   :language: javascript



Response
^^^^^^^^





**Example Update Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/server-update-update-resp.json
   :language: javascript


