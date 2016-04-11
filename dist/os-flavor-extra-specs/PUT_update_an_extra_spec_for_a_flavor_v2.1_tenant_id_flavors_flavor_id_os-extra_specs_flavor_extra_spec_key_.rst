
Update An Extra Spec For A Flavor
=================================

.. rest_method:: PUT /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key}

Updates an extra spec, by key, for a flavor, by ID.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../updateAnExtraSpecForAFlavor.yaml

	- tenant_id: tenant_id
	- flavor_id: flavor_id
	- flavor_extra_spec_key: flavor_extra_spec_key








**Example Update An Extra Spec For A Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-extra-specs/flavor-extra-spec-update-req.json
   :language: javascript



Response
^^^^^^^^





**Example Update An Extra Spec For A Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-extra-specs/flavor-extra-spec-update-resp.json
   :language: javascript


