=============================================================================
List Extra Specs For A Flavor -  OpenStack Compute API v2.1
=============================================================================

List Extra Specs For A Flavor
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_extra_specs_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs.rst#request>`__
`Response <GET_list_extra_specs_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs

Lists all extra specs for a flavor, by ID.



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








**Example List Extra Specs For A Flavor: JSON request**


.. code::

    {
        "extra_specs": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example List Extra Specs For A Flavor: JSON request**


.. code::

    {
        "extra_specs": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    

