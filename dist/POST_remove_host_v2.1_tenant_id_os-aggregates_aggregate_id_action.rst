=============================================================================
Remove Host -  OpenStack Compute API v2.1
=============================================================================

Remove Host
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_remove_host_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#request>`__
`Response <POST_remove_host_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Removes a host from an aggregate.

Specify the ``remove_host`` action in the request body.



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








**Example Remove Host: JSON request**


.. code::

    {
        "remove_host": {
            "host": "bf1454b3d71145d49fca2101c56c728d"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Remove Host: JSON request**


.. code::

    {
        "aggregate": {
            "availability_zone": "nova",
            "created_at": "2013-08-18T12:17:56.990581",
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
    

