=============================================================================
Get Rdp Console (Os-Getrdpconsole Action) -  OpenStack Compute API v2.1
=============================================================================

Get Rdp Console (Os-Getrdpconsole Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_get_rdp_console_(os-getrdpconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_rdp_console_(os-getrdpconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets an `RDP <https://technet.microsoft.com/en-us/windowsserver/ee236407>`__ console for a server.

Specify the ``os-getRDPConsole`` action in the request body.



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
^^^^^^^^^^^^^^^^^^





**Example Get Rdp Console (Os-Getrdpconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "rdp-html5",
            "url": "http://127.0.0.1:6083/?token=191996c3-7b0f-42f3-95a7-f1839f2da6ed"
        }
    }
    

