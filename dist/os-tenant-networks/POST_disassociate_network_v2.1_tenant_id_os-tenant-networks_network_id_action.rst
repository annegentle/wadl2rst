
Disassociate Network
====================

.. rest_method:: POST /v2.1/{tenant_id}/os-tenant-networks/{network_id}/action

Disassociates a network from a project so that the network can be reused.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../disassociateNetwork.yaml

	- tenant_id: tenant_id
	- network_id: network_id








**Example Disassociate Network: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-networks/network-disassociate-req.json
   :language: javascript



Response
^^^^^^^^




