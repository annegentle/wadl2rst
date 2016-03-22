=============================================================================
Get Spice Console (Os-Getspiceconsole Action) -  OpenStack Compute API v2.1
=============================================================================

Get Spice Console (Os-Getspiceconsole Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_get_spice_console_(os-getspiceconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_get_spice_console_(os-getspiceconsole_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a SPICE console for a server.

Specify the ``os-getSPICEConsole`` action in the request body.



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
|os-getSPICEConsole        |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Get Spice Console (Os-Getspiceconsole Action): JSON request**


.. code::

    {
        "os-getSPICEConsole": {
            "type": "spice-html5"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Get Spice Console (Os-Getspiceconsole Action): JSON request**


.. code::

    {
        "console": {
            "type": "spice-html5",
            "url": "http://127.0.0.1:6082/spice_auto.html?token=a30e5d08-6a20-4043-958f-0852440c6af4"
        }
    }
    

