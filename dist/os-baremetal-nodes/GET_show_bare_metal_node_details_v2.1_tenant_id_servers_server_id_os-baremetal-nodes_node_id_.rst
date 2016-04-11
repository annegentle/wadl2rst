
Show Bare Metal Node Details
============================

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/{node_id}

Shows details for a bare metal node.

Preconditions

The bare metal node must be associated with the server.



Normal response codes: 202,,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showBareMetalNodeDetails.yaml

	- tenant_id: tenant_id
	- server_id: server_id
	- node_id: node_id








Response
^^^^^^^^





**Example Show Bare Metal Node Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-baremetal-nodes/baremetal-node-show-resp.json
   :language: javascript


