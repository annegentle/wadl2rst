=============================================================================
Create Volume -  OpenStack Compute API v2.1
=============================================================================

Create Volume
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_volume_v2.1_tenant_id_os-volumes.rst#request>`__
`Response <POST_create_volume_v2.1_tenant_id_os-volumes.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-volumes

Creates a volume.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|display_name              |xsd:string *(Required)*  |The volume name.         |
+--------------------------+-------------------------+-------------------------+
|display_description       |xsd:string *(Required)*  |The volume description.  |
+--------------------------+-------------------------+-------------------------+
|size                      |xsd:string *(Required)*  |The size of the volume,  |
|                          |                         |in gigabytes (GB).       |
+--------------------------+-------------------------+-------------------------+
|volume_type               |xsd:string *(Required)*  |The unique identifier    |
|                          |                         |for a volume type.       |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:string *(Required)*  |One or more metadata key |
|                          |                         |and value pairs to       |
|                          |                         |associate with the       |
|                          |                         |volume.                  |
+--------------------------+-------------------------+-------------------------+
|availability_zone         |xsd:string *(Required)*  |The availability zone.   |
+--------------------------+-------------------------+-------------------------+
|snapshot_id               |xsd:string *(Required)*  |The unique identifier    |
|                          |                         |for a snapshot.          |
+--------------------------+-------------------------+-------------------------+





**Example Create Volume: JSON request**


.. code::

    {
        "volume": {
            "display_name": "vol-001",
            "display_description": "Another volume.",
            "size": 30,
            "volume_type": "289da7f8-6440-407c-9fb4-7db01ec49164",
            "metadata": {
                "contents": "junk"
            },
            "availability_zone": "us-east1"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Volume: JSON request**


.. code::

    {
        "volume": {
            "id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c",
            "display_name": "vol-001",
            "display_description": "Another volume.",
            "status": "active",
            "size": 30,
            "volume_type": "289da7f8-6440-407c-9fb4-7db01ec49164",
            "metadata": {
                "contents": "junk"
            },
            "availability_zone": "us-east1",
            "snapshot_id": null,
            "attachments": [],
            "created_at": "2012-02-14T20:53:07Z"
        }
    }
    

