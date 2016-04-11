
Delete Interface From Bare Metal Node
=====================================

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/action

Deletes an interface from a bare metal node that is associated with a server.



Normal response codes: ,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteInterfaceFromBareMetalNode.yaml

	- tenant_id: tenant_id
	- server_id: server_id








**Example Delete Interface From Bare Metal Node: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-baremetal-nodes/baremetal-node-remove-interface-req.json
   :language: javascript



Response
^^^^^^^^




