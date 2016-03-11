=============================================================================
Delete Quotas -  OpenStack Compute API v2.1
=============================================================================

Delete Quotas
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_quotas_v2_tenant_id_os-quota-sets_tenant_id_.rst#request>`__
`Response <DELETE_delete_quotas_v2_tenant_id_os-quota-sets_tenant_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/os-quota-sets/{tenant_id}

Deletes quotas for a tenant so the quotas revert to default values.



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
|{admin_tenant_id}         |csapi:UUID               |The UUID of the          |
|                          |                         |administrative tenant.   |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




