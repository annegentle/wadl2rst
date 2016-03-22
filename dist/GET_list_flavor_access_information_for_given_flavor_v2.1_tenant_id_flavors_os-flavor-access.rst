=============================================================================
List Flavor Access Information For Given Flavor -  OpenStack Compute API v2.1
=============================================================================

List Flavor Access Information For Given Flavor
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_flavor_access_information_for_given_flavor_v2.1_tenant_id_flavors_os-flavor-access.rst#request>`__
`Response <GET_list_flavor_access_information_for_given_flavor_v2.1_tenant_id_flavors_os-flavor-access.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/flavors/os-flavor-access

Lists flavor access information.



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





**Example List Flavor Access Information For Given Flavor: JSON request**


.. code::

    {
        "flavor_access": [
            {
                "flavor_id": "10",
                "tenant_id": "fake_tenant"
            }
        ]
    }
    

