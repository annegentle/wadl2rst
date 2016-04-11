
Show Port Interface Details
===========================

`Request <GET_show_port_interface_details_v2.1_tenant_id_servers_server_id_os-interface_port_id_.rst#request>`__
`Response <GET_show_port_interface_details_v2.1_tenant_id_servers_server_id_os-interface_port_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-interface/{port_id}

Shows details for a port interface that is attached to a server.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Port Interface Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-interface/port-interface-show-resp.json
   :language: javascript

