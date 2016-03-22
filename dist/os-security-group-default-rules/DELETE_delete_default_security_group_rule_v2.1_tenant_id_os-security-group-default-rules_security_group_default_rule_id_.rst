=============================================================================
Delete Default Security Group Rule -  OpenStack Compute API v2.1
=============================================================================

Delete Default Security Group Rule
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_default_security_group_rule_v2.1_tenant_id_os-security-group-default-rules_security_group_default_rule_id_.rst#request>`__
`Response <DELETE_delete_default_security_group_rule_v2.1_tenant_id_os-security-group-default-rules_security_group_default_rule_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-security-group-default-rules/{security_group_default_rule_id}

Deletes a security group rule.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+---------------------------------+----------------------+---------------------+
|Name                             |Type                  |Description          |
+=================================+======================+=====================+
|{tenant_id}                      |csapi:UUID            |The UUID of the      |
|                                 |                      |tenant in a multi-   |
|                                 |                      |tenancy cloud.       |
+---------------------------------+----------------------+---------------------+
|{security_group_default_rule_id} |csapi:UUID            |The UUID of the      |
|                                 |                      |security group rule. |
+---------------------------------+----------------------+---------------------+








Response
^^^^^^^^^^^^^^^^^^




