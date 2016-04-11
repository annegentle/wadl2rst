
Show Console Details
====================

`Request <GET_show_console_details_v2.1_tenant_id_servers_server_id_consoles_console_id_.rst#request>`__
`Response <GET_show_console_details_v2.1_tenant_id_servers_server_id_consoles_console_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/consoles/{console_id}

Shows details for a console for a server instance.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List consoles: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-consoles/consoles-list-resp.json
   :language: javascript

