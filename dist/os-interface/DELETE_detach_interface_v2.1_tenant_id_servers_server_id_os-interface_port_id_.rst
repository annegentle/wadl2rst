
Detach Interface
================

`Request <DELETE_detach_interface_v2.1_tenant_id_servers_server_id_os-interface_port_id_.rst#request>`__
`Response <DELETE_detach_interface_v2.1_tenant_id_servers_server_id_os-interface_port_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/servers/{server_id}/os-interface/{port_id}

Detaches a port interface.



Normal response codes: 202,,503,400,401,403,405,415,400

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id
	- port_id: port_id







Response
^^^^^^^^




