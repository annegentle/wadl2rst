=============================================================================
Show Console Authentication Token -  OpenStack Compute API v2.1
=============================================================================

Show Console Authentication Token
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_console_authentication_token_v2.1_tenant_id_servers_server_id_os-console-auth-token.rst#request>`__
`Response <GET_show_console_authentication_token_v2.1_tenant_id_servers_server_id_os-console-auth-token.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/os-console-auth-token

Shows the authentication token for a console for a server instance.

This feature is available for ``rdp-html5`` console type only.



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
        "console": {
            "instance_uuid": "b48316c5-71e8-45e4-9884-6c78055b9b13",
            "host": "localhost",
            "port": 5900,
            "internal_access_path": "51af38c3-555e-4884-a314-6c8cdde37444"
        }
    }
    

