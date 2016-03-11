=============================================================================
Delete Security Group Rule -  OpenStack Compute API v2.1
=============================================================================

Delete Security Group Rule
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_security_group_rule_v2.0_security-group-rules_security-group-rules-id_.rst#request>`__
`Response <DELETE_delete_security_group_rule_v2.0_security-group-rules_security-group-rules-id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/security-group-rules/{security-group-rules-id}

Deletes a rule from an OpenStack Networking security group.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{security_group_rule_id}  |csapi:UUID *(Required)*  |The UUID of the security |
|                          |                         |group rule.              |
+--------------------------+-------------------------+-------------------------+








**Example Delete Security Group Rule: JSON request**


.. code::

    DELETE /v2.0/security-group-rules/fc3c327a-b5b5-4cd3-9577-52893289ce08Content-Type: application/jsonAccept: application/json


Response
^^^^^^^^^^^^^^^^^^





**Example Delete Security Group Rule: JSON request**


.. code::

    status: 204

