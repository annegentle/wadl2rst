
Show Network Details
====================

.. rest_method:: GET /v2.1/{tenant_id}/os-networks/{network_id}

Shows details for a network.

Policy defaults enable all users to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showNetworkDetails.yaml

	- tenant_id: tenant_id
	- network_id: network_id








Response
^^^^^^^^





**Example Show Network Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-networks/network-show-resp.json
   :language: javascript


