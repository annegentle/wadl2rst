=============================================================================
List Consistency Group Snapshots With Details -  OpenStack Compute API v2.1
=============================================================================

List Consistency Group Snapshots With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_consistency_group_snapshots_with_details_v2_tenant_id_cgsnapshots_detail.rst#request>`__
`Response <GET_list_consistency_group_snapshots_with_details_v2_tenant_id_cgsnapshots_detail.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/cgsnapshots/detail

Lists all consistency group snapshots with details.



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

+--------------------+-------------+---------------------------------------------+
|Name                |Type         |Description                                  |
+====================+=============+=============================================+
|id                  |csapi:UUID   |The UUID of the consistency group snapshot.  |
|                    |*(Required)* |                                             |
+--------------------+-------------+---------------------------------------------+
|consistencygroup_id |csapi:UUID   |The UUID of the consistency group.           |
|                    |*(Required)* |                                             |
+--------------------+-------------+---------------------------------------------+
|status              |xsd:string   |The ``status`` of the consistency group      |
|                    |*(Required)* |snapshot.                                    |
+--------------------+-------------+---------------------------------------------+
|created_at          |xsd:dateTime |The date and time when the resource was      |
|                    |*(Required)* |created. The date and time stamp format is   |
|                    |             |`ISO 8601                                    |
|                    |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                    |             |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                    |             |``2015-08-27T09:49:58-05:00``. The           |
|                    |             |``±hh:mm`` value, if included, is the time   |
|                    |             |zone as an offset from UTC.                  |
+--------------------+-------------+---------------------------------------------+
|name                |xsd:string   |The consistency group snapshot name.         |
|                    |*(Required)* |                                             |
+--------------------+-------------+---------------------------------------------+
|description         |xsd:string   |The consistency group snapshot description.  |
|                    |*(Required)* |                                             |
+--------------------+-------------+---------------------------------------------+





**Example List Consistency Group Snapshots With Details: JSON request**


.. code::

    {"cgsnapshots": [{"id": "6f519a48-3183-46cf-a32f-41815f813986","consistencygroup_id": "6f519a48-3183-46cf-a32f-41815f814444","status": "available","created_at": "2015-09-16T09:28:52.000000","name": "my-cg1","description": "my first consistency group"},{"id": "aed36625-a6d7-4681-ba59-c7ba3d18c148","consistencygroup_id": "aed36625-a6d7-4681-ba59-c7ba3d18dddd","status": "error","created_at": "2015-09-16T09:31:15.000000","name": "my-cg2","description": "Edited description"}]}

