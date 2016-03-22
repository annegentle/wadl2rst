=============================================================================
Get Serial Console (Os-Getserialconsole Action) -  OpenStack Compute API v2.1
=============================================================================

Get Serial Console (Os-Getserialconsole Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_get_serial_console_(os-getserialconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_serial_console_(os-getserialconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a serial console for a server.

Specify the ``os-getSerialConsole`` action in the request body.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+





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
^^^^^^^^^^^^^^^^^^





**Example Get Serial Console (Os-Getserialconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "serial",
            "url": "ws://127.0.0.1:6083/?token=f9906a48-b71e-4f18-baca-c987da3ebdb3"
        }
    }
    

