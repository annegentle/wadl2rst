=============================================================================
Delete Share -  OpenStack Compute API v2.1
=============================================================================

Delete Share
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_share_v2_tenant_id_shares_share_id_.rst#request>`__
`Response <DELETE_delete_share_v2_tenant_id_shares_share_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/shares/{share_id}

Deletes a share.



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
|{share_id}                |csapi:UUID               |The UUID of the share.   |
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



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|consistency_group_id      |csapi:UUID *(Required)*  |(Since API v2.4.) The    |
|                          |                         |UUID of the consistency  |
|                          |                         |group where the share    |
|                          |                         |was created. You can     |
|                          |                         |omit this parameter if   |
|                          |                         |the share was created    |
|                          |                         |without a consistency    |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^




