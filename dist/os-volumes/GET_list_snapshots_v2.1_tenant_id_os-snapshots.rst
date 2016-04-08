
List Snapshots
==============

`Request <GET_list_snapshots_v2.1_tenant_id_os-snapshots.rst#request>`__
`Response <GET_list_snapshots_v2.1_tenant_id_os-snapshots.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-snapshots

Lists snapshots.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





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
    

