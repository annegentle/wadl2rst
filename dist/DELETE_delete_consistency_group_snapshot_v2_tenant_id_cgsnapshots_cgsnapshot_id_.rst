=============================================================================
Delete Consistency Group Snapshot -  OpenStack Compute API v2.1
=============================================================================

Delete Consistency Group Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_consistency_group_snapshot_v2_tenant_id_cgsnapshots_cgsnapshot_id_.rst#request>`__
`Response <DELETE_delete_consistency_group_snapshot_v2_tenant_id_cgsnapshots_cgsnapshot_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/cgsnapshots/{cgsnapshot_id}

Deletes a consistency group snapshot.



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
|{cgsnapshot_id}           |xsd:string               |The ID of the            |
|                          |                         |consistency group        |
|                          |                         |snapshot.                |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




