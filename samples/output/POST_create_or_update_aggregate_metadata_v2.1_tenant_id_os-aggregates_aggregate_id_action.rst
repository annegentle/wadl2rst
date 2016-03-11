=============================================================================
Create Or Update Aggregate Metadata -  OpenStack Compute API v2.1
=============================================================================

Create Or Update Aggregate Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_or_update_aggregate_metadata_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#request>`__
`Response <POST_create_or_update_aggregate_metadata_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Creates or replaces metadata for an aggregate.

Specify the ``add_metadata`` action in the request body.



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








**Example Create Or Update Aggregate Metadata: JSON request**


.. code::

    {
        "set_metadata": {
            "metadata": {
                "key": "value"
            }
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Or Update Aggregate Metadata: JSON request**


.. code::

    {
        "aggregate": {
            "availability_zone": "nova",
            "created_at": "2013-08-18T12:17:55.959571",
            "deleted": false,
            "deleted_at": null,
            "hosts": [],
            "id": 1,
            "metadata": {
                "availability_zone": "nova",
                "key": "value"
            },
            "name": "name",
            "updated_at": null
        }
    }
    

