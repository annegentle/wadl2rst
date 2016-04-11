
Delete Network
==============

.. rest_method:: DELETE /v2.1/{tenant_id}/os-networks/{network_id}

Deletes a network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteNetwork.yaml

	- tenant_id: tenant_id
	- network_id: network_id








Response
^^^^^^^^




