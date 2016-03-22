=============================================================================
Create Default Security Group Rule -  OpenStack Compute API v2.1
=============================================================================

Create Default Security Group Rule
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_default_security_group_rule_v2.1_tenant_id_os-security-group-default-rules.rst#request>`__
`Response <POST_create_default_security_group_rule_v2.1_tenant_id_os-security-group-default-rules.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-security-group-default-rules

Creates a default security group rule.

If you specify a source port ( ``from_port`` ) or destination port ( ``to_port`` ) value, you must specify an IP protocol ( ``ip_protocol`` ) value. Otherwise, the operation returns the ``Bad Request (400)`` response code.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Create default security  |                         |
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

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |csapi:UUID *(Required)*  |The security group name  |
|                          |                         |or UUID.                 |
+--------------------------+-------------------------+-------------------------+
|ip_protocol               |xsd:string *(Required)*  |The IP protocol. A valid |
|                          |                         |value is ICMP, TCP, or   |
|                          |                         |UDP.                     |
+--------------------------+-------------------------+-------------------------+
|from_port                 |xsd:int *(Required)*     |The port at start of     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|to_port                   |xsd:int *(Required)*     |The port at end of range.|
+--------------------------+-------------------------+-------------------------+
|cidr                      |xsd:string *(Required)*  |The CIDR for address     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+





**Example Create default security group rule: JSON request**


.. code::

    {
        "security_group_default_rule": {
            "ip_protocol": "TCP",
            "from_port": "80",
            "to_port": "80",
            "cidr": "10.10.10.0/24"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|from_port                 |xsd:int *(Required)*     |The port at start of     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID for the         |
|                          |                         |security group.          |
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
|to_port                   |xsd:int *(Required)*     |Port at end of range.    |
+--------------------------+-------------------------+-------------------------+





**Example Create default security group rule: JSON response**


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
    

