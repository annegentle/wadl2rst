
Show Api V2.1
=============

`Request <GET_show_api_v2.1_v2.1.rst#request>`__
`Response <GET_show_api_v2.1_v2.1.rst#response>`__

.. rest_method:: GET /v2.1

Show information about Compute API v2.1.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Api V2.1: JSON request**


.. code::

    {
        "version": {
            "id": "v2.1",
            "links": [
                {
                    "href": "http://openstack.example.com/v2.1/",
                    "rel": "self"
                },
                {
                    "href": "http://docs.openstack.org/",
                    "rel": "describedby",
                    "type": "text/html"
                }
            ],
            "media-types": [
                {
                    "base": "application/json",
                    "type": "application/vnd.openstack.compute+json;version=2.1"
                }
            ],
            "status": "CURRENT",
            "version": "2.21",
            "min_version": "2.1",
            "updated": "2013-07-23T11:33:21Z"
        }
    }
    

