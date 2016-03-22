=============================================================================
Delete Aggregate -  OpenStack Compute API v2.1
=============================================================================

Delete Aggregate
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_aggregate_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#request>`__
`Response <DELETE_delete_aggregate_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-aggregates/{aggregate_id}

Deletes an aggregate.



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
|{aggregate_id}            |xsd:int                  |The aggregate ID.        |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




