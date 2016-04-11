
List Bare Metal Nodes
=====================

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes

Lists the bare metal nodes that are associated with a server.



Normal response codes: 202,,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listBareMetalNodes.yaml

	- tenant_id: tenant_id
	- server_id: server_id








Response
^^^^^^^^





**Example List Bare Metal Nodes: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-baremetal-nodes/baremetal-nodes-list-resp.json
   :language: javascript


