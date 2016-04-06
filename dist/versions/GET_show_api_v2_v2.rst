
Show Api V2
===========

`Request <GET_show_api_v2_v2.rst#request>`__
`Response <GET_show_api_v2_v2.rst#response>`__

.. rest_method:: GET /v2

Show information about Compute API v2.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^









Response
^^^^^^^^





**Example Show Api V2: JSON request**


.. code::

    {
        "version": {
            "id": "v2.0",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/",
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
                    "type": "application/vnd.openstack.compute+json;version=2"
                }
            ],
            "status": "SUPPORTED",
            "version": "",
            "min_version": "",
            "updated": "2011-01-21T11:33:21Z"
        }
    }
    

