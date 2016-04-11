
Create Extra Specs For A Flavor
===============================

.. rest_method:: POST /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs

Creates extra specs for a flavor, by ID.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createExtraSpecsForAFlavor.yaml

	- tenant_id: tenant_id
	- flavor_id: flavor_id








**Example Create Extra Specs For A Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-extra-specs/flavor-extra-spec-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Extra Specs For A Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-extra-specs/flavor-extra-spec-create-resp.json
   :language: javascript


