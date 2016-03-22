=============================================================================
Get Vnc Console (Os-Getvncconsole Action) -  OpenStack Compute API v2.1
=============================================================================

Get Vnc Console (Os-Getvncconsole Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_get_vnc_console_(os-getvncconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_vnc_console_(os-getvncconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a VNC console for a server.

Specify the ``os-getVNCConsole`` action in the request body.



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
|os-getVNCConsole          |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Get Vnc Console (Os-Getvncconsole Action): JSON request**


.. code::

    {
        "os-getVNCConsole": {
            "type": "novnc"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Get Vnc Console (Os-Getvncconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "novnc",
            "url": "http://127.0.0.1:6080/vnc_auto.html?token=191996c3-7b0f-42f3-95a7-f1839f2da6ed"
        }
    }
    

