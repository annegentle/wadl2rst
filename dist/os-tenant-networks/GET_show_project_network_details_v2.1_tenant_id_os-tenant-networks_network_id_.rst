
Show Project Network Details
============================

.. rest_method:: GET /v2.1/{tenant_id}/os-tenant-networks/{network_id}

Shows details for a project network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showProjectNetworkDetails.yaml

	- tenant_id: tenant_id
	- network_id: network_id








Response
^^^^^^^^





**Example Show Project Network Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-tenant-networks/network-show-resp.json
   :language: javascript


