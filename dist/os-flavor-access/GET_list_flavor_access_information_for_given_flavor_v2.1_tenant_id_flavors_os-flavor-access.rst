
List Flavor Access Information For Given Flavor
===============================================

`Request <GET_list_flavor_access_information_for_given_flavor_v2.1_tenant_id_flavors_os-flavor-access.rst#request>`__
`Response <GET_list_flavor_access_information_for_given_flavor_v2.1_tenant_id_flavors_os-flavor-access.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/flavors/os-flavor-access

Lists flavor access information.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Flavor Access Information For Given Flavor: JSON request**


.. code::

    {
        "flavor_access": [
            {
                "flavor_id": "10",
                "tenant_id": "fake_tenant"
            }
        ]
    }
    

