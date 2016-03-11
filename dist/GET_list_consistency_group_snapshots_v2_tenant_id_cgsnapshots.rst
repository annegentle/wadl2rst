=============================================================================
List Consistency Group Snapshots -  OpenStack Compute API v2.1
=============================================================================

List Consistency Group Snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_consistency_group_snapshots_v2_tenant_id_cgsnapshots.rst#request>`__
`Response <GET_list_consistency_group_snapshots_v2_tenant_id_cgsnapshots.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/cgsnapshots

Lists all consistency group snapshots.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |csapi:UUID *(Required)*  |The UUID of the          |
|                          |                         |consistency group        |
|                          |                         |snapshot.                |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The consistency group    |
|                          |                         |snapshot name.           |
+--------------------------+-------------------------+-------------------------+





**Example List Consistency Group Snapshots: JSON request**


.. code::

    {"cgsnapshots": [{"id": "6f519a48-3183-46cf-a32f-41815f813986","name": "my-cg1"},{"id": "aed36625-a6d7-4681-ba59-c7ba3d18c148","name": "my-cg2"}]}

