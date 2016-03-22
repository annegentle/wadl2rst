=============================================================================
Show Ip Details -  OpenStack Compute API v2.1
=============================================================================

Show Ip Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_ip_details_v2.1_tenant_id_servers_server_id_ips_network_label_.rst#request>`__
`Response <GET_show_ip_details_v2.1_tenant_id_servers_server_id_ips_network_label_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/ips/{network_label}

Shows IP addresses details for a network label of a server instance.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
|{network_label}           |xsd:string               |The network label, such  |
|                          |                         |as ``public`` or         |
|                          |                         |``private``.             |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Ip Details: JSON request**


.. code::

    {
        "private": [
            {
                "addr": "192.168.0.3",
                "version": 4
            }
        ]
    }
    

