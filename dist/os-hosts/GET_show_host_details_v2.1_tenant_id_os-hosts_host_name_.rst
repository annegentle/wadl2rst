
Show Host Details
=================

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}

Shows details for a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showHostDetails.yaml

	- tenant_id: tenant_id
	- host_name: host_name








Response
^^^^^^^^





**Example Show Host Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-show-resp.json
   :language: javascript


