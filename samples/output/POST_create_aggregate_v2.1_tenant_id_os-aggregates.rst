=============================================================================
Create Aggregate -  OpenStack Compute API v2.1
=============================================================================

Create Aggregate
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_aggregate_v2.1_tenant_id_os-aggregates.rst#request>`__
`Response <POST_create_aggregate_v2.1_tenant_id_os-aggregates.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-aggregates

Creates an aggregate in an availability zone.



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








**Example Create Aggregate: JSON request**


.. code::

    {
        "aggregate": {
            "name": "name",
            "availability_zone": "nova"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Aggregate: JSON request**


.. code::

    {
        "aggregate": {
            "availability_zone": "nova",
            "created_at": "2013-08-18T12:17:55.751757",
            "deleted": false,
            "deleted_at": null,
            "id": 1,
            "name": "name",
            "updated_at": null
        }
    }
    

