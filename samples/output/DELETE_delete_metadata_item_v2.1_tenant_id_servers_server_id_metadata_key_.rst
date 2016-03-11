=============================================================================
Delete Metadata Item -  OpenStack Compute API v2.1
=============================================================================

Delete Metadata Item
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#request>`__
`Response <DELETE_delete_metadata_item_v2.1_tenant_id_servers_server_id_metadata_key_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/servers/{server_id}/metadata/{key}

Deletes a metadata item, by key, from a server.

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
|{key}                     |xsd:string               |The metadata item key,   |
|                          |                         |as a string. Maximum     |
|                          |                         |length is 255 characters.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




