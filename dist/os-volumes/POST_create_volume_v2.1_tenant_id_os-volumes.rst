
Create Volume
=============

`Request <POST_create_volume_v2.1_tenant_id_os-volumes.rst#request>`__
`Response <POST_create_volume_v2.1_tenant_id_os-volumes.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-volumes

Creates a volume.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: createVolume.yaml

	- volume: volume
	- display_name: display_name
	- display_description: display_description
	- size: size
	- volume_type: volume_type
	- metadata: metadata
	- availability_zone: availability_zone
	- snapshot_id: snapshot_id




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
^^^^^^^^





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
    

