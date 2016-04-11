
Create Interface
================

`Request <POST_create_interface_v2.1_tenant_id_servers_server_id_os-interface.rst#request>`__
`Response <POST_create_interface_v2.1_tenant_id_servers_server_id_os-interface.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/os-interface

Creates a port interface and uses it to attach a port to a server instance.



Normal response codes: 200,,503,400,401,403,405,415,400

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../createInterface.yaml

	- interfaceAttachment: interfaceAttachment
	- port_id: port_id
	- net_id: net_id
	- fixed_ips: fixed_ips




**Example Create Interface: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-interface/port-interface-create-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../createInterface.yaml

	- interfaceAttachment: interfaceAttachment
	- fixed_ips: fixed_ips
	- mac_addr: mac_addr
	- net_id: net_id
	- port_id: port_id
	- port_state: port_state




**Example Create Interface: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-interface/port-interface-create-resp.json
   :language: javascript

