=============================================================================
Create Flavor -  OpenStack Compute API v2.1
=============================================================================

Create Flavor
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_flavor_v2.1_tenant_id_flavors.rst#request>`__
`Response <POST_create_flavor_v2.1_tenant_id_flavors.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/flavors

Creates a flavor.



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
^^^^^^^^^^^^^^^^^^





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
    

