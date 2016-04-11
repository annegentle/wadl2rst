
Get Rdp Console (Os-Getrdpconsole Action)
=========================================

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets an `RDP <https://technet.microsoft.com/en-us/windowsserver/ee236407>`__ console for a server.

Specify the ``os-getRDPConsole`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../getRdpConsole(Os-GetrdpconsoleAction).yaml

	- tenant_id: tenant_id
	- server_id: server_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../getRdpConsole(Os-GetrdpconsoleAction).yaml

	- os-getRDPConsole: os-getRDPConsole




**Example Get Rdp Console (Os-Getrdpconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getRDPConsole-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Get Rdp Console (Os-Getrdpconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getRDPConsole-create-resp.json
   :language: javascript


