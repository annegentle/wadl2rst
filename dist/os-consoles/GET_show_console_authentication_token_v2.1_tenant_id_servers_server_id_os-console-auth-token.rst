
Show Console Authentication Token
=================================

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-console-auth-token

Shows the authentication token for a console for a server instance.

This feature is available for ``rdp-html5`` console type only.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showConsoleAuthenticationToken.yaml

	- tenant_id: tenant_id
	- server_id: server_id








Response
^^^^^^^^





**Example List consoles: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-consoles/console-auth-show-resp.json
   :language: javascript


