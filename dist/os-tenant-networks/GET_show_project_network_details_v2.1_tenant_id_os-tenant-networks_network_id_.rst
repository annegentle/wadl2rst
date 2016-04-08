
Show Project Network Details
============================

`Request <GET_show_project_network_details_v2.1_tenant_id_os-tenant-networks_network_id_.rst#request>`__
`Response <GET_show_project_network_details_v2.1_tenant_id_os-tenant-networks_network_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-tenant-networks/{network_id}

Shows details for a project network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Project Network Details: JSON request**


.. code::

    {
        "networks": [
            {
                "cidr": "10.0.0.0/29",
                "id": "616fb98f-46ca-475e-917e-2563e5a8cd19",
                "label": "test_0"
            },
            {
                "cidr": "10.0.0.8/29",
                "id": "616fb98f-46ca-475e-917e-2563e5a8cd20",
                "label": "test_1"
            }
        ]
    }
    

