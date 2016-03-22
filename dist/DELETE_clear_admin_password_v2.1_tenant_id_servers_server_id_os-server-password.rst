=============================================================================
Clear Admin Password -  OpenStack Compute API v2.1
=============================================================================

Clear Admin Password
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_clear_admin_password_v2.1_tenant_id_servers_server_id_os-server-password.rst#request>`__
`Response <DELETE_clear_admin_password_v2.1_tenant_id_servers_server_id_os-server-password.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/servers/{server_id}/os-server-password

Clears the encrypted administrative password for a server, which removes it from the metadata server.

This action does not actually change the instance server password.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
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




