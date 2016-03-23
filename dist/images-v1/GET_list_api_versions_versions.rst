=============================================================================
List Api Versions -  OpenStack Image API v1
=============================================================================

List Api Versions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_api_versions_versions.rst#request>`__
`Response <GET_list_api_versions_versions.rst#response>`__

.. code-block:: javascript

    GET //versions

Shows details for the Image service API v1.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^





**Example List Api Versions: JSON request**


.. code::

    {
        "versions": [
            {
                "status": "EXPERIMENTAL",
                "id": "v3.0",
                "links": [
                    {
                        "href": "http://23.253.228.211:9292/v3/",
                        "rel": "self"
                    }
                ]
            },
            {
                "status": "CURRENT",
                "id": "v2.3",
                "links": [
                    {
                        "href": "http://23.253.228.211:9292/v2/",
                        "rel": "self"
                    }
                ]
            },
            {
                "status": "SUPPORTED",
                "id": "v2.2",
                "links": [
                    {
                        "href": "http://23.253.228.211:9292/v2/",
                        "rel": "self"
                    }
                ]
            },
            {
                "status": "SUPPORTED",
                "id": "v2.1",
                "links": [
                    {
                        "href": "http://23.253.228.211:9292/v2/",
                        "rel": "self"
                    }
                ]
            },
            {
                "status": "SUPPORTED",
                "id": "v2.0",
                "links": [
                    {
                        "href": "http://23.253.228.211:9292/v2/",
                        "rel": "self"
                    }
                ]
            },
            {
                "status": "SUPPORTED",
                "id": "v1.1",
                "links": [
                    {
                        "href": "http://23.253.228.211:9292/v1/",
                        "rel": "self"
                    }
                ]
            },
            {
                "status": "SUPPORTED",
                "id": "v1.0",
                "links": [
                    {
                        "href": "http://23.253.228.211:9292/v1/",
                        "rel": "self"
                    }
                ]
            }
        ]
    }
    

