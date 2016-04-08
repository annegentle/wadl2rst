
Create Extra Specs For A Flavor
===============================

`Request <POST_create_extra_specs_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs.rst#request>`__
`Response <POST_create_extra_specs_for_a_flavor_v2.1_tenant_id_flavors_flavor_id_os-extra_specs.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs

Creates extra specs for a flavor, by ID.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Extra Specs For A Flavor: JSON request**


.. code::

    {
        "extra_specs": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    


Response
^^^^^^^^





**Example Create Extra Specs For A Flavor: JSON request**


.. code::

    {
        "extra_specs": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    

