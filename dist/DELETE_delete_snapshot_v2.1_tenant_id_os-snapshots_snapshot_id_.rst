=============================================================================
Delete Snapshot -  OpenStack Compute API v2.1
=============================================================================

Delete Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_snapshot_v2.1_tenant_id_os-snapshots_snapshot_id_.rst#request>`__
`Response <DELETE_delete_snapshot_v2.1_tenant_id_os-snapshots_snapshot_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-snapshots/{snapshot_id}

Deletes a snapshot from the account.

This operation is asynchronous. You must list snapshots repeatedly to determine whether the snapshot was deleted.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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








Response
^^^^^^^^^^^^^^^^^^





**Example Delete Snapshot: JSON request**


.. code::

    HTTP/1.1 202 Accepted
    Content-Type: text/html; charset=UTF-8
    Content-Length: 0
    Date: Mon, 01 Dec 2014 16:23:10 GMT
    

