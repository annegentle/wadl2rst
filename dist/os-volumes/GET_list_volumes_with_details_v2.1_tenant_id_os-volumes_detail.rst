
List Volumes With Details
=========================

`Request <GET_list_volumes_with_details_v2.1_tenant_id_os-volumes_detail.rst#request>`__
`Response <GET_list_volumes_with_details_v2.1_tenant_id_os-volumes_detail.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-volumes/detail

Lists all volumes with details.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





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
    

