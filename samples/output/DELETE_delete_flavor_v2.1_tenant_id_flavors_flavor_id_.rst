=============================================================================
Delete Flavor -  OpenStack Compute API v2.1
=============================================================================

Delete Flavor
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_flavor_v2.1_tenant_id_flavors_flavor_id_.rst#request>`__
`Response <DELETE_delete_flavor_v2.1_tenant_id_flavors_flavor_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/flavors/{flavor_id}

Deletes a flavor.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
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




