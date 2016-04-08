
Show Flavor Details
===================

`Request <GET_show_flavor_details_v2.1_tenant_id_flavors_flavor_id_.rst#request>`__
`Response <GET_show_flavor_details_v2.1_tenant_id_flavors_flavor_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/flavors/{flavor_id}

Shows details for a flavor.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Flavor Details: JSON request**


.. code::

    {
        "flavor": {
            "OS-FLV-DISABLED:disabled": false,
            "disk": 1,
            "OS-FLV-EXT-DATA:ephemeral": 0,
            "os-flavor-access:is_public": true,
            "id": "1",
            "links": [
                {
                    "href": "http://openstack.example.com/v2.1/openstack/flavors/1",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/flavors/1",
                    "rel": "bookmark"
                }
            ],
            "name": "m1.tiny",
            "ram": 512,
            "swap": "",
            "vcpus": 1
        }
    }
    

