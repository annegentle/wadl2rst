=============================================================================
Delete Share Server -  OpenStack Compute API v2.1
=============================================================================

Delete Share Server
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_share_server_v2_tenant_id_share-servers_share_server_id_.rst#request>`__
`Response <DELETE_delete_share_server_v2_tenant_id_share-servers_share_server_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/share-servers/{share_server_id}

Deletes a share server.

An administrator can delete an active share server only if it contains no dependent shares.



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
|{share_server_id}         |csapi:UUID               |The UUID of the share    |
|                          |                         |server.                  |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|X-Openstack-Manila-Api-   |xsd:string               |The HTTP header to       |
|Version                   |                         |specify a valid Shared   |
|                          |                         |File Systems API micro-  |
|                          |                         |version. For example,    |
|                          |                         |``"X-Openstack-Manila-   |
|                          |                         |Api-Version: 2.6"``. If  |
|                          |                         |you omit this header,    |
|                          |                         |the default micro-       |
|                          |                         |version is 2.0.          |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




