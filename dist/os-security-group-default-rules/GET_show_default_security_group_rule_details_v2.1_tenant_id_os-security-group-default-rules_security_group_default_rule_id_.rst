
Show Default Security Group Rule Details
========================================

`Request <GET_show_default_security_group_rule_details_v2.1_tenant_id_os-security-group-default-rules_security_group_default_rule_id_.rst#request>`__
`Response <GET_show_default_security_group_rule_details_v2.1_tenant_id_os-security-group-default-rules_security_group_default_rule_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-security-group-default-rules/{security_group_default_rule_id}

Shows details for a security group rule.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- security_group_default_rule_id: security_group_default_rule_id







Response
^^^^^^^^


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
|ip_range                  |xsd:dict *(Required)*    |An IP range object.      |
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
    

