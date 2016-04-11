
List Port Interfaces
====================

`Request <GET_list_port_interfaces_v2.1_tenant_id_servers_server_id_os-interface.rst#request>`__
`Response <GET_list_port_interfaces_v2.1_tenant_id_servers_server_id_os-interface.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-interface

Lists port interfaces that are attached to a server.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: ../listPortInterfaces.yaml

	- interfaceAttachment: interfaceAttachment
	- port_state: port_state
	- fixed_ips: fixed_ips
	- mac_addr: mac_addr
	- net_id: net_id
	- port_id: port_id




**Example List Port Interfaces: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-interface/port-interfaces-list-resp.json
   :language: javascript

