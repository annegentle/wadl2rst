
Delete Project Network
======================

`Request <DELETE_delete_project_network_v2.1_tenant_id_os-tenant-networks_network_id_.rst#request>`__
`Response <DELETE_delete_project_network_v2.1_tenant_id_os-tenant-networks_network_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/os-tenant-networks/{network_id}

Deletes a project network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- network_id: network_id







Response
^^^^^^^^




