=============================================================================
List Volumes -  OpenStack Compute API v2.1
=============================================================================

List Volumes
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_volumes_v2.1_tenant_id_os-volumes.rst#request>`__
`Response <GET_list_volumes_v2.1_tenant_id_os-volumes.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-volumes

Lists the volumes associated with the account.



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





**Example List Volumes: JSON request**


.. code::

    {
        "volumes": [
            {
                "id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c",
                "display_name": "vol-001",
                "display_description": "Another volume.",
                "size": 30,
                "volume_type": "289da7f8-6440-407c-9fb4-7db01ec49164",
                "metadata": {
                    "contents": "junk"
                },
                "availability_zone": "us-east1",
                "snapshot_id": null,
                "attachments": [],
                "created_at": "2012-02-14T20:53:07Z"
            },
            {
                "id": "76b8950a-8594-4e5b-8dce-0dfa9c696358",
                "display_name": "vol-002",
                "display_description": "Yet another volume.",
                "size": 25,
                "volume_type": "96c3bda7-c82a-4f50-be73-ca7621794835",
                "metadata": {},
                "availability_zone": "us-east2",
                "snapshot_id": null,
                "attachments": [],
                "created_at": "2012-03-15T19:10:03Z"
            }
        ]
    }
    

