
Show Extension Details
======================

`Request <GET_show_extension_details_v2.1_tenant_id_extensions_alias_.rst#request>`__
`Response <GET_show_extension_details_v2.1_tenant_id_extensions_alias_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/extensions/{alias}

Shows details for an extension, by alias.



Normal response codes: 200,203

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







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

