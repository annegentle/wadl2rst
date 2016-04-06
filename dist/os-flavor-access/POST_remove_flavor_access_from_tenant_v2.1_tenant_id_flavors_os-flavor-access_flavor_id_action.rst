
Remove Flavor Access From Tenant
================================

`Request <POST_remove_flavor_access_from_tenant_v2.1_tenant_id_flavors_os-flavor-access_flavor_id_action.rst#request>`__
`Response <POST_remove_flavor_access_from_tenant_v2.1_tenant_id_flavors_os-flavor-access_flavor_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/flavors/os-flavor-access/{flavor_id}/action

Removes flavor access from a tenant and flavor.

Specify the ``removeTenantAccess`` action and the ``tenant_id`` in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- flavor_id: flavor_id







**Example Remove Flavor Access From Tenant: JSON request**


.. code::

    {
        "removeTenantAccess": {
            "tenant": "fake_tenant"
        }
    }
    


Response
^^^^^^^^





**Example Remove Flavor Access From Tenant: JSON request**


.. code::

    {
        "flavor_access": []
    }
    

