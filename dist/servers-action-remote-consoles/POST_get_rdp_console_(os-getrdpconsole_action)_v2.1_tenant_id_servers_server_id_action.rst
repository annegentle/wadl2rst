
Get Rdp Console (Os-Getrdpconsole Action)
=========================================

`Request <POST_get_rdp_console_(os-getrdpconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_rdp_console_(os-getrdpconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets an `RDP <https://technet.microsoft.com/en-us/windowsserver/ee236407>`__ console for a server.

Specify the ``os-getRDPConsole`` action in the request body.



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
|os-getRDPConsole          |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Get Rdp Console (Os-Getrdpconsole Action): JSON request**


.. code::

    {
        "os-getRDPConsole": {
            "type": "rdp-html5"
        }
    }
    


Response
^^^^^^^^





**Example Get Rdp Console (Os-Getrdpconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "rdp-html5",
            "url": "http://127.0.0.1:6083/?token=191996c3-7b0f-42f3-95a7-f1839f2da6ed"
        }
    }
    

