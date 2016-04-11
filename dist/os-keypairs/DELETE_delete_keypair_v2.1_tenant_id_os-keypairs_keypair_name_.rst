
Delete Keypair
==============

.. rest_method:: DELETE /v2.1/{tenant_id}/os-keypairs/{keypair_name}

Deletes a keypair.



Normal response codes: 204

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteKeypair.yaml

	- tenant_id: tenant_id
	- keypair_name: keypair_name








Response
^^^^^^^^




