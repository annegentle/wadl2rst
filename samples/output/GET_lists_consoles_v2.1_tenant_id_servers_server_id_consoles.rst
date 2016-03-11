=============================================================================
Lists Consoles -  OpenStack Compute API v2.1
=============================================================================

Lists Consoles
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_lists_consoles_v2.1_tenant_id_servers_server_id_consoles.rst#request>`__
`Response <GET_lists_consoles_v2.1_tenant_id_servers_server_id_consoles.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/consoles

Lists all consoles for a server instance.



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
    

