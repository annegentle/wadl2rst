=============================================================================
List Snapshots With Details -  OpenStack Compute API v2.1
=============================================================================

List Snapshots With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_snapshots_with_details_v2.1_tenant_id_os-snapshots_detail.rst#request>`__
`Response <GET_list_snapshots_with_details_v2.1_tenant_id_os-snapshots_detail.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-snapshots/detail

Lists all snapshots with details.



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





**Example List Snapshots With Details: JSON request**


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
    

