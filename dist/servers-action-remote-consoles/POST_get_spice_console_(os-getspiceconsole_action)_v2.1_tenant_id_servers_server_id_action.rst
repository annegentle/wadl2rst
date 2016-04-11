
Get Spice Console (Os-Getspiceconsole Action)
=============================================

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a SPICE console for a server.

Specify the ``os-getSPICEConsole`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../getSpiceConsole(Os-GetspiceconsoleAction).yaml

	- tenant_id: tenant_id
	- server_id: server_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../getSpiceConsole(Os-GetspiceconsoleAction).yaml

	- os-getSPICEConsole: os-getSPICEConsole




**Example Get Spice Console (Os-Getspiceconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getSPICEConsole-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Get Spice Console (Os-Getspiceconsole Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/getSPICEConsole-create-resp.json
   :language: javascript


