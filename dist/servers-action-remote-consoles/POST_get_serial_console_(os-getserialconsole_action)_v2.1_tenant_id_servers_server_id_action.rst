
Get Serial Console (Os-Getserialconsole Action)
===============================================

`Request <POST_get_serial_console_(os-getserialconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_serial_console_(os-getserialconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a serial console for a server.

Specify the ``os-getSerialConsole`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../getSerialConsole(Os-GetserialconsoleAction).yaml

	- os-getSerialConsole: os-getSerialConsole




**Example Get Serial Console (Os-Getserialconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getSerialConsole-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Get Serial Console (Os-Getserialconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getSerialConsole-create-resp.json
   :language: javascript

