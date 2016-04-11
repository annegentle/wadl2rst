
Delete Console
==============

.. rest_method:: DELETE /v2.1/{tenant_id}/servers/{server_id}/consoles/{console_id}

Deletes a console for a server instance.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteConsole.yaml

	- tenant_id: tenant_id
	- server_id: server_id
	- console_id: console_id








Response
^^^^^^^^




