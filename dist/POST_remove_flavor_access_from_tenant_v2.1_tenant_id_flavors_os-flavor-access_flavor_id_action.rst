=============================================================================
Remove Flavor Access From Tenant -  OpenStack Compute API v2.1
=============================================================================

Remove Flavor Access From Tenant
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_remove_flavor_access_from_tenant_v2.1_tenant_id_flavors_os-flavor-access_flavor_id_action.rst#request>`__
`Response <POST_remove_flavor_access_from_tenant_v2.1_tenant_id_flavors_os-flavor-access_flavor_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/flavors/os-flavor-access/{flavor_id}/action

Removes flavor access from a tenant and flavor.

Specify the ``removeTenantAccess`` action and the ``tenant_id`` in the request body.



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








**Example Remove Flavor Access From Tenant: JSON request**


.. code::

    {
        "removeTenantAccess": {
            "tenant": "fake_tenant"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Remove Flavor Access From Tenant: JSON request**


.. code::

    {
        "flavor_access": []
    }
    

