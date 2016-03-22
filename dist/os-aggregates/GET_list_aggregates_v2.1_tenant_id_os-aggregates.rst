=============================================================================
List Aggregates -  OpenStack Compute API v2.1
=============================================================================

List Aggregates
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_aggregates_v2.1_tenant_id_os-aggregates.rst#request>`__
`Response <GET_list_aggregates_v2.1_tenant_id_os-aggregates.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-aggregates

Lists all aggregates. Includes the ID, name, and availability zone for each aggregate.



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








**Example List Aggregates: JSON request**


.. code::

    {
        "aggregate": {
            "name": "name",
            "availability_zone": "nova"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example List Aggregates: JSON request**


.. code::

    {
        "aggregates": [
            {
                "availability_zone": "nova",
                "created_at": "2013-08-18T12:17:56.856455",
                "deleted": false,
                "deleted_at": null,
                "hosts": [],
                "id": 1,
                "metadata": {
                    "availability_zone": "nova"
                },
                "name": "name",
                "updated_at": null
            }
        ]
    }
    

