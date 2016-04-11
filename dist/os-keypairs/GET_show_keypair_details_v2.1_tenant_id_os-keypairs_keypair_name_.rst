
Show Keypair Details
====================

.. rest_method:: GET /v2.1/{tenant_id}/os-keypairs/{keypair_name}

Shows details for a keypair that is associated with the account.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showKeypairDetails.yaml

	- tenant_id: tenant_id
	- keypair_name: keypair_name








Response
^^^^^^^^





**Example Show Keypair Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-keypairs/keypair-show-resp.json
   :language: javascript


