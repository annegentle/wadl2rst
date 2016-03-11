=============================================================================
Force-Delete Share Snapshot -  OpenStack Compute API v2.1
=============================================================================

Force-Delete Share Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_force-delete_share_snapshot_v2_tenant_id_snapshots_snapshot_id_action.rst#request>`__
`Response <POST_force-delete_share_snapshot_v2_tenant_id_snapshots_snapshot_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/snapshots/{snapshot_id}/action

Administrator only. Force-deletes a share snapshot in any state.

Use the ``policy.json`` file to grant permissions for this action to other roles.



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
|{snapshot_id}             |csapi:UUID               |The UUID of the snapshot.|
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-force_delete           |xsd:string *(Required)*  |To force-delete a        |
|                          |                         |snapshot, set this value |
|                          |                         |to ``null``. The force-  |
|                          |                         |delete action, unlike    |
|                          |                         |the delete action,       |
|                          |                         |ignores the snapshot     |
|                          |                         |status.                  |
+--------------------------+-------------------------+-------------------------+





**Example Force-Delete Share Snapshot: JSON request**


.. code::

    {"os-force_delete": null}


Response
^^^^^^^^^^^^^^^^^^




