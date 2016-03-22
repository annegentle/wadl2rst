=============================================================================
Show Default Security Group Rule Details -  OpenStack Compute API v2.1
=============================================================================

Show Default Security Group Rule Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_default_security_group_rule_details_v2.1_tenant_id_os-security-group-default-rules_security_group_default_rule_id_.rst#request>`__
`Response <GET_show_default_security_group_rule_details_v2.1_tenant_id_os-security-group-default-rules_security_group_default_rule_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-security-group-default-rules/{security_group_default_rule_id}

Shows details for a security group rule.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Show default security    |                         |
|                          |group rule: JSON response|                         |
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


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|from_port                 |xsd:int *(Required)*     |The port at start of     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the security |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|ip_protocol               |xsd:string *(Required)*  |The IP protocol. A valid |
|                          |                         |value is ICMP, TCP, or   |
|                          |                         |UDP.                     |
+--------------------------+-------------------------+-------------------------+
|ip_range                  |xsd:string *(Required)*  |An IP range object.      |
+--------------------------+-------------------------+-------------------------+
|cidr                      |xsd:string *(Required)*  |The CIDR for address     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|to_port                   |xsd:int *(Required)*     |The port at end of range.|
+--------------------------+-------------------------+-------------------------+





**Example Show default security group rule: JSON response**


.. code::

    {
        "security_group_default_rule": {
            "from_port": 80,
            "id": 1,
            "ip_protocol": "TCP",
            "ip_range": {
                "cidr": "10.10.10.0/24"
            },
            "to_port": 80
        }
    }
    

