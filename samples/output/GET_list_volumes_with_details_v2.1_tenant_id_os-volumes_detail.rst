=============================================================================
List Volumes With Details -  OpenStack Compute API v2.1
=============================================================================

List Volumes With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_volumes_with_details_v2.1_tenant_id_os-volumes_detail.rst#request>`__
`Response <GET_list_volumes_with_details_v2.1_tenant_id_os-volumes_detail.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-volumes/detail

Lists all volumes with details.



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





**Example List Volumes With Details: JSON request**


.. code::

    {
        "volumes": [
            {
                "attachments": [
                    {
                        "device": "/",
                        "id": "a26887c6-c47b-4654-abb5-dfadf7d3f803",
                        "serverId": "3912f2b4-c5ba-4aec-9165-872876fe202e",
                        "volumeId": "a26887c6-c47b-4654-abb5-dfadf7d3f803"
                    }
                ],
                "availabilityZone": "zone1:host1",
                "createdAt": "1999-01-01T01:01:01.000000",
                "displayDescription": "Volume Description",
                "displayName": "Volume Name",
                "id": "a26887c6-c47b-4654-abb5-dfadf7d3f803",
                "metadata": {},
                "size": 100,
                "snapshotId": null,
                "status": "in-use",
                "volumeType": "Backup"
            }
        ]
    }
    

