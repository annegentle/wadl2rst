
Delete Bare Metal Node
======================

`Request <DELETE_delete_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_node_id_.rst#request>`__
`Response <DELETE_delete_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_node_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/{node_id}

Deletes a bare metal node from a server.



Normal response codes: 202,,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id
	- node_id: node_id







Response
^^^^^^^^




