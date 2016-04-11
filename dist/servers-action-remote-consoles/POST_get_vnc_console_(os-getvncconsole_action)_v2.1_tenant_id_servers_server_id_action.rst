
Get Vnc Console (Os-Getvncconsole Action)
=========================================

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a VNC console for a server.

Specify the ``os-getVNCConsole`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../getVncConsole(Os-GetvncconsoleAction).yaml

	- tenant_id: tenant_id
	- server_id: server_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../getVncConsole(Os-GetvncconsoleAction).yaml

	- os-getVNCConsole: os-getVNCConsole




**Example Get Vnc Console (Os-Getvncconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getVNCConsole-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Get Vnc Console (Os-Getvncconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getVNCConsole-create-resp.json
   :language: javascript


