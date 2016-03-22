=============================================================================
List Default Security Group Rules -  OpenStack Compute API v2.1
=============================================================================

List Default Security Group Rules
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_default_security_group_rules_v2.1_tenant_id_os-security-group-default-rules.rst#request>`__
`Response <GET_list_default_security_group_rules_v2.1_tenant_id_os-security-group-default-rules.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-security-group-default-rules

Lists default security group rules.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |List default security    |                         |
|                          |group rules: JSON        |                         |
|                          |response                 |                         |
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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|from_port                 |xsd:int *(Required)*     |Port at start of range.  |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the security |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|ip_protocol               |xsd:string *(Required)*  |The IP protocol: ICMP,   |
|                          |                         |TCP, or UDP.             |
+--------------------------+-------------------------+-------------------------+
|ip_range                  |xsd:string *(Required)*  |An IP range object.      |
+--------------------------+-------------------------+-------------------------+
|cidr                      |xsd:string *(Required)*  |The CIDR for address     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|to_port                   |xsd:int *(Required)*     |Port at end of range.    |
+--------------------------+-------------------------+-------------------------+





**Example List default security group rules: JSON response**


.. code::

    {
        "security_group_default_rules": [
            {
                "from_port": 80,
                "id": 1,
                "ip_protocol": "TCP",
                "ip_range": {
                    "cidr": "10.10.10.0/24"
                },
                "to_port": 80
            }
        ]
    }
    

