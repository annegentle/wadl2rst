
List Flavors With Details
=========================

`Request <GET_list_flavors_with_details_v2.1_tenant_id_flavors_detail.rst#request>`__
`Response <GET_list_flavors_with_details_v2.1_tenant_id_flavors_detail.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/flavors/detail

Lists flavors with details.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: listFlavorsWithDetails.yaml

	- minDisk: minDisk
	- minRam: minRam
	- sort_key: sort_key
	- sort_dir: sort_dir
	- limit: limit
	- marker: marker






Response
^^^^^^^^





**Example List Flavors With Details: JSON request**


.. code::

    {
        "flavors": [
            {
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
            },
            {
                "OS-FLV-DISABLED:disabled": false,
                "disk": 20,
                "OS-FLV-EXT-DATA:ephemeral": 0,
                "os-flavor-access:is_public": true,
                "id": "2",
                "links": [
                    {
                        "href": "http://openstack.example.com/v2.1/openstack/flavors/2",
                        "rel": "self"
                    },
                    {
                        "href": "http://openstack.example.com/openstack/flavors/2",
                        "rel": "bookmark"
                    }
                ],
                "name": "m1.small",
                "ram": 2048,
                "swap": "",
                "vcpus": 1
            },
            {
                "OS-FLV-DISABLED:disabled": false,
                "disk": 40,
                "OS-FLV-EXT-DATA:ephemeral": 0,
                "os-flavor-access:is_public": true,
                "id": "3",
                "links": [
                    {
                        "href": "http://openstack.example.com/v2.1/openstack/flavors/3",
                        "rel": "self"
                    },
                    {
                        "href": "http://openstack.example.com/openstack/flavors/3",
                        "rel": "bookmark"
                    }
                ],
                "name": "m1.medium",
                "ram": 4096,
                "swap": "",
                "vcpus": 2
            },
            {
                "OS-FLV-DISABLED:disabled": false,
                "disk": 80,
                "OS-FLV-EXT-DATA:ephemeral": 0,
                "os-flavor-access:is_public": true,
                "id": "4",
                "links": [
                    {
                        "href": "http://openstack.example.com/v2.1/openstack/flavors/4",
                        "rel": "self"
                    },
                    {
                        "href": "http://openstack.example.com/openstack/flavors/4",
                        "rel": "bookmark"
                    }
                ],
                "name": "m1.large",
                "ram": 8192,
                "swap": "",
                "vcpus": 4
            },
            {
                "OS-FLV-DISABLED:disabled": false,
                "disk": 160,
                "OS-FLV-EXT-DATA:ephemeral": 0,
                "os-flavor-access:is_public": true,
                "id": "5",
                "links": [
                    {
                        "href": "http://openstack.example.com/v2.1/openstack/flavors/5",
                        "rel": "self"
                    },
                    {
                        "href": "http://openstack.example.com/openstack/flavors/5",
                        "rel": "bookmark"
                    }
                ],
                "name": "m1.xlarge",
                "ram": 16384,
                "swap": "",
                "vcpus": 8
            }
        ]
    }
    

