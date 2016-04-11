
List Keypairs
=============

.. rest_method:: GET /v2.1/{tenant_id}/os-keypairs

Lists keypairs that are associated with the account.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listKeypairs.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example List Keypairs: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-keypairs/keypairs-list-resp.json
   :language: javascript


