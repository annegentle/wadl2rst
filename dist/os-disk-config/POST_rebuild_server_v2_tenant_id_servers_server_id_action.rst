
Rebuild Server
==============

.. rest_method:: POST /v2/{tenant_id}/servers/{server_id}/action

Rebuilds a server.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../rebuildServer.yaml

	- tenant_id: tenant_id
	- os-disk-config:diskConfig: os-disk-config:diskConfig
	- server_id: server_id








**Example Rebuild Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/server-action-rebuild-req.json
   :language: javascript



Response
^^^^^^^^





**Example Rebuild Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/server-action-rebuild-resp.json
   :language: javascript


