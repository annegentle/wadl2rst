
Add Flavor Access To Tenant
===========================

.. rest_method:: POST /v2.1/{tenant_id}/flavors/os-flavor-access/{flavor_id}/action

Adds flavor access to a tenant and flavor.

Specify the ``addTenantAccess`` action and the ``tenant_id`` in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../addFlavorAccessToTenant.yaml

	- tenant_id: tenant_id
	- flavor_id: flavor_id








**Example Add Flavor Access To Tenant: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-access/flavor-access-add-req.json
   :language: javascript



Response
^^^^^^^^





**Example Add Flavor Access To Tenant: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-flavor-access/flavor-access-add-resp.json
   :language: javascript


