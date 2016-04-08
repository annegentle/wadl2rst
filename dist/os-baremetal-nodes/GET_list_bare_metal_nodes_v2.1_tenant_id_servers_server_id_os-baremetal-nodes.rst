
List Bare Metal Nodes
=====================

`Request <GET_list_bare_metal_nodes_v2.1_tenant_id_servers_server_id_os-baremetal-nodes.rst#request>`__
`Response <GET_list_bare_metal_nodes_v2.1_tenant_id_servers_server_id_os-baremetal-nodes.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes

Lists the bare metal nodes that are associated with a server.



Normal response codes: 202,,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Bare Metal Nodes: JSON request**


.. code::

    {
        "nodes": [
            {
                "cpus": 8,
                "id": 1,
                "instance_uuid": null,
                "interfaces": [
                    {
                        "address": "aa:aa:aa:aa:aa:aa",
                        "datapath_id": null,
                        "id": 1,
                        "port_no": null
                    }
                ],
                "local_gb": 128,
                "memory_mb": 8192,
                "pm_address": "10.1.2.3",
                "pm_user": "pm_user",
                "pxe_config_path": null,
                "service_host": "host",
                "task_state": null,
                "terminal_port": 8000,
                "updated_at": null,
                "uuid": "6fae68da-108b-4a9d-87c4-88831ee1241b"
            }
        ]
    }
    

