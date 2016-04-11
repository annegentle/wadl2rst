
Show Extension Details
======================

.. rest_method:: GET /v2.1/{tenant_id}/extensions/{alias}

Shows details for an extension, by alias.



Normal response codes: 200,203

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showExtensionDetails.yaml

	- tenant_id: tenant_id
	- alias: alias








Response
^^^^^^^^


.. rest_parameters:: ../showExtensionDetails.yaml

	- extension: extension
	- name: name
	- alias: alias
	- links: links
	- namespace: namespace
	- description: description
	- updated: updated




**Example Show Extension Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/extensions/extension-show-resp.json
   :language: javascript


