
Create Or Import Keypair
========================

`Request <POST_create_or_import_keypair_v2.1_tenant_id_os-keypairs.rst#request>`__
`Response <POST_create_or_import_keypair_v2.1_tenant_id_os-keypairs.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-keypairs

Generates or imports a keypair.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../createOrImportKeypair.yaml

	- name: name
	- public_key: public_key




**Example Create Or Import Keypair: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-keypairs/keypair-import-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Or Import Keypair: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-keypairs/keypair-import-resp.json
   :language: javascript

