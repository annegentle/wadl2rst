
List Actions For Server
=======================

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-instance-actions

Lists actions for a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listActionsForServer.yaml

	- tenant_id: tenant_id
	- server_id: server_id








Response
^^^^^^^^





**Example List Actions For Server: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-instance-actions/instance-actions-list-resp.json
   :language: javascript


