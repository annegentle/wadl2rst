=============================================================================
Show Aggregate Details -  OpenStack Compute API v2.1
=============================================================================

Show Aggregate Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_aggregate_details_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#request>`__
`Response <GET_show_aggregate_details_v2.1_tenant_id_os-aggregates_aggregate_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-aggregates/{aggregate_id}

Shows details for an aggregate. Details include hosts and metadata.



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








**Example Show Aggregate Details: JSON request**


.. code::

    {
        "aggregate": {
            "name": "name",
            "availability_zone": "nova"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Show Aggregate Details: JSON request**


.. code::

    {
        "aggregate": {
            "availability_zone": "nova",
            "created_at": "2013-08-18T12:17:56.380226",
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
    }
    

