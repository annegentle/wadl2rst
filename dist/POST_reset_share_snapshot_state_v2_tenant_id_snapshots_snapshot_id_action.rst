=============================================================================
Reset Share Snapshot State -  OpenStack Compute API v2.1
=============================================================================

Reset Share Snapshot State
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_reset_share_snapshot_state_v2_tenant_id_snapshots_snapshot_id_action.rst#request>`__
`Response <POST_reset_share_snapshot_state_v2_tenant_id_snapshots_snapshot_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/snapshots/{snapshot_id}/action

Administrator only. Explicitly updates the state of a share snapshot.

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
|status                    |xsd:string *(Required)*  |The snapshot status,     |
|                          |                         |which is ``available``,  |
|                          |                         |``error``, ``creating``, |
|                          |                         |``deleting``, or         |
|                          |                         |``error_deleting``.      |
+--------------------------+-------------------------+-------------------------+





**Example Reset Share Snapshot State: JSON request**


.. code::

    {"os-reset_status": {"status": "error"}}


Response
^^^^^^^^^^^^^^^^^^




