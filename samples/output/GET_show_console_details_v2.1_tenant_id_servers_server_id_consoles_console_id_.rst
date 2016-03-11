=============================================================================
Show Console Details -  OpenStack Compute API v2.1
=============================================================================

Show Console Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_console_details_v2.1_tenant_id_servers_server_id_consoles_console_id_.rst#request>`__
`Response <GET_show_console_details_v2.1_tenant_id_servers_server_id_consoles_console_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/consoles/{console_id}

Shows details for a console for a server instance.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |List consoles: JSON      |                         |
|                          |response                 |                         |
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
|{console_id}              |csapi:UUID               |The UUID of the console. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List consoles: JSON response**


.. code::

    {
        "consoles": [
            {
                "console": {
                    "console_type": "fake",
                    "id": 1
                }
            }
        ]
    }
    

