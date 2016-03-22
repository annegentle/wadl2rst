=============================================================================
Delete Assisted Volume Snapshot -  OpenStack Compute API v2.1
=============================================================================

Delete Assisted Volume Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_assisted_volume_snapshot_v2.1_tenant_id_os-assisted-volume-snapshots_snapshot_id_.rst#request>`__
`Response <DELETE_delete_assisted_volume_snapshot_v2.1_tenant_id_os-assisted-volume-snapshots_snapshot_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-assisted-volume-snapshots/{snapshot_id}

Deletes an assisted volume snapshot.

To make this request, add the ``delete_info`` query parameter to the URI, as follows:

DELETE /os-assisted-volume-snapshots?delete_info='{"volume_id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c"}'

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
|{snapshot_id}             |csapi:UUID               |The UUID of the snapshot.|
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+-------------------+-------------------+--------------------------------------+
|Name               |Type               |Description                           |
+===================+===================+======================================+
|delete_info        |xsd:string         |Information for snapshot deletion.    |
|                   |*(Required)*       |Include the ID of the associated      |
|                   |                   |volume. For example: DELETE /os-      |
|                   |                   |assisted-volume-                      |
|                   |                   |snapshots?delete_info='{"volume_id":  |
|                   |                   |"521752a6-acf6-4b2d-bc7a-             |
|                   |                   |119f9148cd8c"}'                       |
+-------------------+-------------------+--------------------------------------+







Response
^^^^^^^^^^^^^^^^^^




