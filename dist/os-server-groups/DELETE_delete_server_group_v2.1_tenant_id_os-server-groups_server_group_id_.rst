
Delete Server Group
===================

.. rest_method:: DELETE /v2.1/{tenant_id}/os-server-groups/{server_group_id}

Deletes a server group.



Normal response codes: 204,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteServerGroup.yaml

	- tenant_id: tenant_id
	- server_group_id: server_group_id








Response
^^^^^^^^




