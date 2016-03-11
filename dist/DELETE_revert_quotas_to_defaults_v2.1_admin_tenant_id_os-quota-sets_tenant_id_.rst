=============================================================================
Revert Quotas To Defaults -  OpenStack Compute API v2.1
=============================================================================

Revert Quotas To Defaults
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_revert_quotas_to_defaults_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#request>`__
`Response <DELETE_revert_quotas_to_defaults_v2.1_admin_tenant_id_os-quota-sets_tenant_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}

Reverts the quotas to default values for a project or a project and a user.

To revert quotas for a project and a user, specify the ``user_id`` query parameter.



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
|{admin_tenant_id}         |csapi:UUID               |The UUID of the          |
|                          |                         |administrative tenant.   |
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|user_id                   |xsd:string *(Required)*  |Filters the response by  |
|                          |                         |a user, by ID.           |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^




