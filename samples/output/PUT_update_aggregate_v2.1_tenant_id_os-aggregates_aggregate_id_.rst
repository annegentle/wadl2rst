=============================================================================
Update Aggregate -  OpenStack Compute API v2.1
=============================================================================

Update Aggregate
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_aggregate_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#request>`__
`Response <PUT_update_aggregate_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/os-aggregates/{aggregate_id}

Updates either or both the name and availability zone for an aggregate.



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








**Example Update Aggregate: JSON request**


.. code::

    {
        "aggregate": {
            "name": "newname",
            "availability_zone": "nova2"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Update Aggregate: JSON request**


.. code::

    {
        "aggregate": {
            "availability_zone": "nova2",
            "created_at": "2013-08-18T12:17:56.259751",
            "deleted": false,
            "deleted_at": null,
            "hosts": [],
            "id": 1,
            "metadata": {
                "availability_zone": "nova2"
            },
            "name": "newname",
            "updated_at": "2013-08-18T12:17:56.286720"
        }
    }
    

