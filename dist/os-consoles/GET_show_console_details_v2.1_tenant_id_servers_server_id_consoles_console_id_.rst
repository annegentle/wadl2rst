
Show Console Details
====================

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/consoles/{console_id}

Shows details for a console for a server instance.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showConsoleDetails.yaml

	- tenant_id: tenant_id
	- server_id: server_id
	- console_id: console_id








Response
^^^^^^^^





**Example List consoles: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-consoles/consoles-list-resp.json
   :language: javascript


