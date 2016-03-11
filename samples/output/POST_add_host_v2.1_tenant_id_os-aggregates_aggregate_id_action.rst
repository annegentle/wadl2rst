=============================================================================
Add Host -  OpenStack Compute API v2.1
=============================================================================

Add Host
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_add_host_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#request>`__
`Response <POST_add_host_v2.1_tenant_id_os-aggregates_aggregate_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Adds a host to an aggregate.

Specify the ``add_host`` action in the request body.



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








**Example Add Host: JSON request**


.. code::

    {
        "add_host": {
            "host": "21549b2f665945baaa7101926a00143c"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Add Host: JSON request**


.. code::

    {
        "aggregate": {
            "availability_zone": "nova",
            "created_at": "2013-08-18T12:17:56.297823",
            "deleted": false,
            "deleted_at": null,
            "hosts": [
                "21549b2f665945baaa7101926a00143c"
            ],
            "id": 1,
            "metadata": {
                "availability_zone": "nova"
            },
            "name": "name",
            "updated_at": null
        }
    }
    

