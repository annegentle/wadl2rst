
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-getSerialConsole       |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Get Serial Console (Os-Getserialconsole Action): JSON request**


.. code::

    {
        "os-getSerialConsole": {
            "type": "serial"
        }
    }
    


Response
^^^^^^^^





**Example Get Serial Console (Os-Getserialconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "serial",
            "url": "ws://127.0.0.1:6083/?token=f9906a48-b71e-4f18-baca-c987da3ebdb3"
        }
    }
    

