
Add Flavor Access To Tenant
===========================

`Request <POST_add_flavor_access_to_tenant_v2.1_tenant_id_flavors_os-flavor-access_flavor_id_action.rst#request>`__
`Response <POST_add_flavor_access_to_tenant_v2.1_tenant_id_flavors_os-flavor-access_flavor_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/flavors/os-flavor-access/{flavor_id}/action

Adds flavor access to a tenant and flavor.

Specify the ``addTenantAccess`` action and the ``tenant_id`` in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Add Flavor Access To Tenant: JSON request**


.. code::

    {
        "addTenantAccess": {
            "tenant": "fake_tenant"
        }
    }
    


Response
^^^^^^^^





**Example Add Flavor Access To Tenant: JSON request**


.. code::

    {
        "flavor_access": [
            {
                "flavor_id": "10",
                "tenant_id": "fake_tenant"
            }
        ]
    }
    

