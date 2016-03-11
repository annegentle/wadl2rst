=============================================================================
Show Consistency Group Snapshot Details -  OpenStack Compute API v2.1
=============================================================================

Show Consistency Group Snapshot Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_consistency_group_snapshot_details_v2_tenant_id_cgsnapshots_cgsnapshot_id_.rst#request>`__
`Response <GET_show_consistency_group_snapshot_details_v2_tenant_id_cgsnapshots_cgsnapshot_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/cgsnapshots/{cgsnapshot_id}

Shows details for a consistency group snapshot.



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
|{cgsnapshot_id}           |xsd:string               |The ID of the            |
|                          |                         |consistency group        |
|                          |                         |snapshot.                |
+--------------------------+-------------------------+-------------------------+
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





**Example Show Consistency Group Snapshot Details: JSON request**


.. code::

    {"cgsnapshot": {"id": "6f519a48-3183-46cf-a32f-41815f813986","consistencygroup_id": "6f519a48-3183-46cf-a32f-41815f814444","status": "available","created_at": "2015-09-16T09:28:52.000000","name": "my-cg1","description": "my first consistency group"}}

