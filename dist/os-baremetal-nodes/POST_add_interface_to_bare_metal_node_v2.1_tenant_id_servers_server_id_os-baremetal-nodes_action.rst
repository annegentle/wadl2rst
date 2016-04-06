
Add Interface To Bare Metal Node
================================

`Request <POST_add_interface_to_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_action.rst#request>`__
`Response <POST_add_interface_to_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/action

Adds an interface to a bare metal node that is associated with a server.



Normal response codes: 202,,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id







**Example Add Interface To Bare Metal Node: JSON request**


.. code::

    {
        "add_interface": {
            "address": "aa:aa:aa:aa:aa:aa"
        }
    }
    


Response
^^^^^^^^





**Example Add Interface To Bare Metal Node: JSON request**


.. code::

    {
        "interface": {
            "address": "aa:aa:aa:aa:aa:aa",
            "datapath_id": null,
            "id": 1,
            "port_no": null
        }
    }
    

