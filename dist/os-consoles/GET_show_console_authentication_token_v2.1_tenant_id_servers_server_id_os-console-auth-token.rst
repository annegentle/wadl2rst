
Show Console Authentication Token
=================================

`Request <GET_show_console_authentication_token_v2.1_tenant_id_servers_server_id_os-console-auth-token.rst#request>`__
`Response <GET_show_console_authentication_token_v2.1_tenant_id_servers_server_id_os-console-auth-token.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-console-auth-token

Shows the authentication token for a console for a server instance.

This feature is available for ``rdp-html5`` console type only.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List consoles: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-consoles/console-auth-show-resp.json
   :language: javascript

