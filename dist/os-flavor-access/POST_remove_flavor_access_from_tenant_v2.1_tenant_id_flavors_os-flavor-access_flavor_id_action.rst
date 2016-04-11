
Remove Flavor Access From Tenant
================================

.. rest_method:: POST /v2.1/{tenant_id}/flavors/os-flavor-access/{flavor_id}/action

Removes flavor access from a tenant and flavor.

Specify the ``removeTenantAccess`` action and the ``tenant_id`` in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../removeFlavorAccessFromTenant.yaml

	- tenant_id: tenant_id
	- flavor_id: flavor_id








**Example Remove Flavor Access From Tenant: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-access/flavor-access-remove-req.json
   :language: javascript



Response
^^^^^^^^





**Example Remove Flavor Access From Tenant: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-access/flavor-access-remove-resp.json
   :language: javascript


