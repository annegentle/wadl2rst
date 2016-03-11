=============================================================================
Show Flavor Details -  OpenStack Compute API v2.1
=============================================================================

Show Flavor Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_flavor_details_v2.1_tenant_id_flavors_flavor_id_.rst#request>`__
`Response <GET_show_flavor_details_v2.1_tenant_id_flavors_flavor_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/flavors/{flavor_id}

Shows details for a flavor.



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
|{flavor_id}               |xsd:int                  |The ID of the flavor.    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





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
    

