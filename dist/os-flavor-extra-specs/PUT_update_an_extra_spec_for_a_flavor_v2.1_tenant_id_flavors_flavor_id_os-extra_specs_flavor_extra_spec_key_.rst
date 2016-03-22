=============================================================================
Update An Extra Spec For A Flavor -  OpenStack Compute API v2.1
=============================================================================

Update An Extra Spec For A Flavor
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_an_extra_spec_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs_flavor_extra_spec_key_.rst#request>`__
`Response <PUT_update_an_extra_spec_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs_flavor_extra_spec_key_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key}

Updates an extra spec, by key, for a flavor, by ID.



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
|{flavor_extra_spec_key}   |xsd:string               |The extra spec key for   |
|                          |                         |the flavor.              |
+--------------------------+-------------------------+-------------------------+








**Example Update An Extra Spec For A Flavor: JSON request**


.. code::

    {
        "key1": "new_value1"
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Update An Extra Spec For A Flavor: JSON request**


.. code::

    {
        "key1": "new_value1"
    }
    

