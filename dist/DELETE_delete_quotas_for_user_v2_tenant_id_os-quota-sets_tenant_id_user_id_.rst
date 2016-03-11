=============================================================================
Delete Quotas For User -  OpenStack Compute API v2.1
=============================================================================

Delete Quotas For User
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_quotas_for_user_v2_tenant_id_os-quota-sets_tenant_id_user_id_.rst#request>`__
`Response <DELETE_delete_quotas_for_user_v2_tenant_id_os-quota-sets_tenant_id_user_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/os-quota-sets/{tenant_id}/{user_id}

Deletes quotas for a user so that the quotas revert to default values.



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
|{user_id}                 |xsd:string *(Required)*  |The user ID. Specify in  |
|                          |                         |the URI as               |
|                          |                         |``user_id={user_id}``.   |
+--------------------------+-------------------------+-------------------------+
|{admin_tenant_id}         |csapi:UUID               |The UUID of the          |
|                          |                         |administrative tenant.   |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




