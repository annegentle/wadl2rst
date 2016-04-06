
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







**Example Create Flavor: JSON request**


.. code::

    {
        "flavor": {
            "name": "test_flavor",
            "ram": 1024,
            "vcpus": 2,
            "disk": 10,
            "id": "10"
        }
    }
    


Response
^^^^^^^^





**Example Create Flavor: JSON request**


.. code::

    {
        "flavor": {
            "OS-FLV-DISABLED:disabled": false,
            "disk": 10,
            "OS-FLV-EXT-DATA:ephemeral": 0,
            "os-flavor-access:is_public": true,
            "id": "10",
            "links": [
                {
                    "href": "http://openstack.example.com/v2.1/flavors/10",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/flavors/10",
                    "rel": "bookmark"
                }
            ],
            "name": "test_flavor",
            "ram": 1024,
            "swap": "",
            "vcpus": 2
        }
    }
    

