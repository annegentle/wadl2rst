
Show An Extra Spec For A Flavor
===============================

`Request <GET_show_an_extra_spec_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs_flavor_extra_spec_key_.rst#request>`__
`Response <GET_show_an_extra_spec_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs_flavor_extra_spec_key_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key}

Shows an extra spec, by key, for a flavor, by ID.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show An Extra Spec For A Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-extra-specs/flavor-extra-spec-show-resp.json
   :language: javascript

