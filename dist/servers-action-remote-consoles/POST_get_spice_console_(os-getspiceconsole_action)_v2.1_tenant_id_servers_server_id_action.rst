
Get Spice Console (Os-Getspiceconsole Action)
=============================================

`Request <POST_get_spice_console_(os-getspiceconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_spice_console_(os-getspiceconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a SPICE console for a server.

Specify the ``os-getSPICEConsole`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: getSpiceConsole(Os-GetspiceconsoleAction).yaml

	- os-getSPICEConsole: os-getSPICEConsole




**Example Get Spice Console (Os-Getspiceconsole Action): JSON request**


.. code::

    {
        "os-getSPICEConsole": {
            "type": "spice-html5"
        }
    }
    


Response
^^^^^^^^





**Example Get Spice Console (Os-Getspiceconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "spice-html5",
            "url": "http://127.0.0.1:6082/spice_auto.html?token=a30e5d08-6a20-4043-958f-0852440c6af4"
        }
    }
    

