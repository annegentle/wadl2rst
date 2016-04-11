
Add Bare Metal Node
===================

`Request <POST_add_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes.rst#request>`__
`Response <POST_add_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes

Adds a bare metal node to a server.

Preconditions

You can add a bare metal node to a server with an ``ACTIVE``, ``PAUSED``, ``SHUTOFF``, ``VERIFY_RESIZE``, or ``SOFT_DELETED`` status.

You can add a bare metal node to a server with a status that is not locked.



Normal response codes: 202,,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Add Bare Metal Node: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-baremetal-nodes/baremetal-node-create-req.json
   :language: javascript



**Example Add Bare Metal Node: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-baremetal-nodes/baremetal-node-create-with-address-req.json
   :language: javascript



Response
^^^^^^^^





**Example Add Bare Metal Node: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-baremetal-nodes/baremetal-node-create-resp.json
   :language: javascript



**Example Add Bare Metal Node: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-baremetal-nodes/baremetal-node-create-with-address-resp.json
   :language: javascript

