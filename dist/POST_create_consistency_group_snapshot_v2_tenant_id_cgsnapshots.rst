=============================================================================
Create Consistency Group Snapshot -  OpenStack Compute API v2.1
=============================================================================

Create Consistency Group Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_consistency_group_snapshot_v2_tenant_id_cgsnapshots.rst#request>`__
`Response <POST_create_consistency_group_snapshot_v2_tenant_id_cgsnapshots.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/cgsnapshots

Creates a consistency group snapshot.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The consistency group    |
|                          |                         |snapshot name.           |
+--------------------------+-------------------------+-------------------------+





**Example Create Consistency Group Snapshot: JSON request**


.. code::

    {"cgsnapshot": {"consistencygroup_id": "6f519a48-3183-46cf-a32f-41815f814546","name": "firstcg","description": "first consistency group","user_id": "6f519a48-3183-46cf-a32f-41815f814444","project_id": "6f519a48-3183-46cf-a32f-41815f815555","status": "creating"}}


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





**Example Create Consistency Group Snapshot: JSON request**


.. code::

    {"cgsnapshot": {"id": "6f519a48-3183-46cf-a32f-41815f816666","name": "firstcg"}}

