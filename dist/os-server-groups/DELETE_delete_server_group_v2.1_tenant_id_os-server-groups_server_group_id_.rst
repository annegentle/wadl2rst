
Delete Server Group
===================

`Request <DELETE_delete_server_group_v2.1_tenant_id_os-server-groups_server_group_id_.rst#request>`__
`Response <DELETE_delete_server_group_v2.1_tenant_id_os-server-groups_server_group_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/os-server-groups/{server_group_id}

Deletes a server group.



Normal response codes: 204,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_group_id: server_group_id







Response
^^^^^^^^




