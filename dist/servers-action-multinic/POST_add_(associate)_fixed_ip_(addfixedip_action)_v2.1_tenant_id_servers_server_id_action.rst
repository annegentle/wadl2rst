=============================================================================
Add (Associate) Fixed Ip (Addfixedip Action) -  OpenStack Compute API v2.1
=============================================================================

Add (Associate) Fixed Ip (Addfixedip Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_add_(associate)_fixed_ip_(addfixedip_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_add_(associate)_fixed_ip_(addfixedip_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Adds a fixed IP address to a server instance, which associates that address with the server. The fixed IP address is retrieved from the network that you specify in the request.

Specify the ``addFixedIp`` action and the network ID in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
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
|addFixedIp                |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Add (Associate) Fixed Ip (Addfixedip Action): JSON request**


.. code::

    


Response
^^^^^^^^^^^^^^^^^^




