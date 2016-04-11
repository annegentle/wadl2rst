
Resize Server
=============

.. rest_method:: POST /v2/{tenant_id}/servers/{server_id}/action

Resizes a server.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../resizeServer.yaml

	- tenant_id: tenant_id
	- os-disk-config:diskConfig: os-disk-config:diskConfig
	- server_id: server_id








**Example Resize Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/server-resize-create-req.json
   :language: javascript



Response
^^^^^^^^




