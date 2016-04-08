
Get Vnc Console (Os-Getvncconsole Action)
=========================================

`Request <POST_get_vnc_console_(os-getvncconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_vnc_console_(os-getvncconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a VNC console for a server.

Specify the ``os-getVNCConsole`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: getVncConsole(Os-GetvncconsoleAction).yaml

	- os-getVNCConsole: os-getVNCConsole




**Example Get Vnc Console (Os-Getvncconsole Action): JSON request**


.. code::

    {
        "os-getVNCConsole": {
            "type": "novnc"
        }
    }
    


Response
^^^^^^^^





**Example Get Vnc Console (Os-Getvncconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "novnc",
            "url": "http://127.0.0.1:6080/vnc_auto.html?token=191996c3-7b0f-42f3-95a7-f1839f2da6ed"
        }
    }
    

