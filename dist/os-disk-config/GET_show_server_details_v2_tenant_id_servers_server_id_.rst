
Show Server Details
===================

.. rest_method:: GET /v2/{tenant_id}/servers/{server_id}

Shows details for a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showServerDetails.yaml

	- tenant_id: tenant_id
	- os-disk-config:diskConfig: os-disk-config:diskConfig
	- server_id: server_id








Response
^^^^^^^^


.. rest_parameters:: ../showServerDetails.yaml

	- os-disk-config:diskConfig: os-disk-config:diskConfig




**Example Show Server Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/server-get-resp.json
   :language: javascript


