
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id


This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|minDisk                   |xsd:int *(Required)*     |Filters the response by  |
|                          |                         |a minimum disk space, in |
|                          |                         |GB.                      |
+--------------------------+-------------------------+-------------------------+
|minRam                    |xsd:int *(Required)*     |Filters the response by  |
|                          |                         |a minimum RAM, in MB.    |
+--------------------------+-------------------------+-------------------------+
|sort_key                  |xsd:string *(Required)*  |Sorts by a server        |
|                          |                         |attribute. Default       |
|                          |                         |attribute is             |
|                          |                         |``created``. You can     |
|                          |                         |specify multiple pairs   |
|                          |                         |of sort key and sort     |
|                          |                         |direction query          |
|                          |                         |parameters. If you omit  |
|                          |                         |the sort direction in a  |
|                          |                         |pair, the API uses the   |
|                          |                         |natural sorting          |
|                          |                         |direction of the server  |
|                          |                         |``sort_key`` attribute.  |
+--------------------------+-------------------------+-------------------------+
|sort_dir                  |xsd:string *(Required)*  |Sort direction. A valid  |
|                          |                         |value is ``asc``         |
|                          |                         |(ascending) or ``desc``  |
|                          |                         |(descending). Default is |
|                          |                         |``desc``. You can        |
|                          |                         |specify multiple pairs   |
|                          |                         |of sort key and sort     |
|                          |                         |direction query          |
|                          |                         |parameters. If you omit  |
|                          |                         |the sort direction in a  |
|                          |                         |pair, the API uses the   |
|                          |                         |natural sorting          |
|                          |                         |direction of the         |
|                          |                         |direction of the server  |
|                          |                         |``sort_key`` attribute.  |
+--------------------------+-------------------------+-------------------------+
|limit                     |xsd:int *(Required)*     |Requests a page size of  |
|                          |                         |items. Returns a number  |
|                          |                         |of items up to a limit   |
|                          |                         |value. Use the ``limit`` |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+
|marker                    |xsd:string *(Required)*  |The ID of the last-seen  |
|                          |                         |item. Use the ``limit``  |
|                          |                         |parameter to make an     |
|                          |                         |initial limited request  |
|                          |                         |and use the ID of the    |
|                          |                         |last-seen item from the  |
|                          |                         |response as the          |
|                          |                         |``marker`` parameter     |
|                          |                         |value in a subsequent    |
|                          |                         |limited request.         |
+--------------------------+-------------------------+-------------------------+







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
    

