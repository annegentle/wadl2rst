
Create Flavor
=============

`Request <POST_create_flavor_v2.1_tenant_id_flavors.rst#request>`__
`Response <POST_create_flavor_v2.1_tenant_id_flavors.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/flavors

Creates a flavor.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/flavors/flavor-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/flavors/flavor-create-resp.json
   :language: javascript

