=============================================================================
Delete Project Network -  OpenStack Compute API v2.1
=============================================================================

Delete Project Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_project_network_v2.1_tenant_id_os-tenant-networks_network_id_.rst#request>`__
`Response <DELETE_delete_project_network_v2.1_tenant_id_os-tenant-networks_network_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-tenant-networks/{network_id}

Deletes a project network.

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
|{network_id}              |csapi:UUID               |The UUID of the network. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




