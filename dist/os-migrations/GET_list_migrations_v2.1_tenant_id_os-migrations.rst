
List Migrations
===============

`Request <GET_list_migrations_v2.1_tenant_id_os-migrations.rst#request>`__
`Response <GET_list_migrations_v2.1_tenant_id_os-migrations.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-migrations

Lists in-progress migrations.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Migrations: JSON request**


.. code::

    {
        "migrations": [
            {
                "created_at": "2012-10-29T13:42:02.000000",
                "dest_compute": "compute2",
                "dest_host": "192.0.2.0",
                "dest_node": "node2",
                "id": 1234,
                "instance_uuid": "instance_id_123",
                "new_instance_type_id": 2,
                "old_instance_type_id": 1,
                "source_compute": "compute1",
                "source_node": "node1",
                "status": "Done",
                "updated_at": "2012-10-29T13:42:02.000000"
            },
            {
                "created_at": "2013-10-22T13:42:02.000000",
                "dest_compute": "compute20",
                "dest_host": "5.6.7.8",
                "dest_node": "node20",
                "id": 5678,
                "instance_uuid": "instance_id_456",
                "new_instance_type_id": 6,
                "old_instance_type_id": 5,
                "source_compute": "compute10",
                "source_node": "node10",
                "status": "Done",
                "updated_at": "2013-10-22T13:42:02.000000"
            }
        ]
    }
    

