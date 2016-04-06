
Create Snapshot
===============

`Request <POST_create_snapshot_v2.1_tenant_id_os-snapshots.rst#request>`__
`Response <POST_create_snapshot_v2.1_tenant_id_os-snapshots.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-snapshots

Creates a snapshot.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|snapshot                  |xsd:string *(Required)*  |A partial representation |
|                          |                         |of a snapshot that is    |
|                          |                         |used to create a         |
|                          |                         |snapshot.                |
+--------------------------+-------------------------+-------------------------+





**Example Create Snapshot: JSON request**


.. code::

    {
        "snapshot": {
            "display_name": "snap-001",
            "display_description": "Daily backup",
            "volume_id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c",
            "force": false
        }
    }
    


Response
^^^^^^^^





**Example Create Snapshot: JSON request**


.. code::

    {
        "snapshot": {
            "createdAt": "2013-02-25T16:27:54.724209",
            "displayDescription": "Default description",
            "displayName": "Default name",
            "id": "100",
            "size": 100,
            "status": "available",
            "volumeId": 12
        }
    }
    

