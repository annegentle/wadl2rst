
List Api Versions
=================

`Request <GET_list_api_versions_.rst#request>`__
`Response <GET_list_api_versions_.rst#response>`__

.. rest_method:: GET /

Lists information about all Compute API versions.



Normal response codes: 200,300

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^









Response
^^^^^^^^





**Example List Api Versions: JSON request**


.. code::

    {
        "versions": [
            {
                "id": "v2.0",
                "links": [
                    {
                        "href": "http://openstack.example.com/v2/",
                        "rel": "self"
                    }
                ],
                "status": "SUPPORTED",
                "version": "",
                "min_version": "",
                "updated": "2011-01-21T11:33:21Z"
            },
            {
                "id": "v2.1",
                "links": [
                    {
                        "href": "http://openstack.example.com/v2.1/",
                        "rel": "self"
                    }
                ],
                "status": "CURRENT",
                "version": "2.14",
                "min_version": "2.1",
                "updated": "2013-07-23T11:33:21Z"
            }
        ]
    }
    

