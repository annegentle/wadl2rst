=============================================================================
Delete Security Group Rule -  OpenStack Compute API v2.1
=============================================================================

Delete Security Group Rule
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_security_group_rule_v2.1_tenant_id_os-security-group-rules_security_group_rule_id_.rst#request>`__
`Response <DELETE_delete_security_group_rule_v2.1_tenant_id_os-security-group-rules_security_group_rule_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-security-group-rules/{security_group_rule_id}

Deletes a security group rule.



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
|{security_group_rule_id}  |xsd:int                  |The ID of the security   |
|                          |                         |group rule.              |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




