=============================================================================
List Snapshots -  OpenStack Compute API v2.1
=============================================================================

List Snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_snapshots_v2.1_tenant_id_os-snapshots.rst#request>`__
`Response <GET_list_snapshots_v2.1_tenant_id_os-snapshots.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-snapshots

Lists snapshots.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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








Response
^^^^^^^^^^^^^^^^^^





**Example List Snapshots: JSON request**


.. code::

    {
        "snapshots": [
            {
                "createdAt": "2013-02-25T16:27:54.684999",
                "displayDescription": "Default description",
                "displayName": "Default name",
                "id": 100,
                "size": 100,
                "status": "available",
                "volumeId": 12
            },
            {
                "createdAt": "2013-02-25T16:27:54.685005",
                "displayDescription": "Default description",
                "displayName": "Default name",
                "id": 101,
                "size": 100,
                "status": "available",
                "volumeId": 12
            },
            {
                "createdAt": "2013-02-25T16:27:54.685008",
                "displayDescription": "Default description",
                "displayName": "Default name",
                "id": 102,
                "size": 100,
                "status": "available",
                "volumeId": 12
            }
        ]
    }
    

