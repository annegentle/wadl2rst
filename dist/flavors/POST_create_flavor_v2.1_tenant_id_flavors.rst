
Create Flavor
=============

.. rest_method:: POST /v2.1/{tenant_id}/flavors

Creates a flavor.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createFlavor.yaml

	- tenant_id: tenant_id








**Example Create Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/flavors/flavor-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Flavor: JSON request**


.. literalinclude:: ../../../doc/api_samples/flavors/flavor-create-resp.json
   :language: javascript


