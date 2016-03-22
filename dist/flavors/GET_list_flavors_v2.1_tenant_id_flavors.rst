=============================================================================
List Flavors -  OpenStack Compute API v2.1
=============================================================================

List Flavors
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_flavors_v2.1_tenant_id_flavors.rst#request>`__
`Response <GET_list_flavors_v2.1_tenant_id_flavors.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/flavors

Lists flavors.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Flavors: JSON request**


.. code::

    {
        "flavors": [
            {
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
                "name": "m1.tiny"
            },
            {
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
                "name": "m1.small"
            },
            {
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
                "name": "m1.medium"
            },
            {
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
                "name": "m1.large"
            },
            {
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
                "name": "m1.xlarge"
            }
        ]
    }
    

