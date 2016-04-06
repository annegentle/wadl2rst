
Create Security Group Rule
==========================

`Request <POST_create_security_group_rule_v2.1_tenant_id_os-security-group-rules.rst#request>`__
`Response <POST_create_security_group_rule_v2.1_tenant_id_os-security-group-rules.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-security-group-rules

Creates a rule for a security group.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group_rule       |xsd:dict *(Required)*    |A                        |
|                          |                         |``security_group_rule``  |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|parent_group_id           |csapi:UUID *(Required)*  |Security group ID.       |
+--------------------------+-------------------------+-------------------------+
|ip_protocol               |xsd:string *(Required)*  |The IP protocol: ICMP,   |
|                          |                         |TCP, or UDP.             |
+--------------------------+-------------------------+-------------------------+
|from_port                 |xsd:int *(Required)*     |The port at start of     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|to_port                   |xsd:int *(Required)*     |The port at end of range.|
+--------------------------+-------------------------+-------------------------+
|cidr                      |xsd:string *(Required)*  |The CIDR for address     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|group_id                  |csapi:UUID *(Required)*  |The source security      |
|                          |                         |group ID.                |
+--------------------------+-------------------------+-------------------------+





**Example Create security group rule: JSON request**


.. code::

    {
        "security_group_rule": {
            "from_port": "443",
            "ip_protocol": "tcp",
            "to_port": "443",
            "cidr": "0.0.0.0/0",
            "parent_group_id": "48700ff3-30b8-4e63-845f-a79c9633e9fb"
        }
    }
    


Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group_rule       |xsd:dict *(Required)*    |A                        |
|                          |                         |``security_group_rule``  |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|ip_protocol               |xsd:string *(Required)*  |The IP protocol: ICMP,   |
|                          |                         |TCP, or UDP.             |
+--------------------------+-------------------------+-------------------------+
|from_port                 |xsd:int *(Required)*     |Port at start of range.  |
+--------------------------+-------------------------+-------------------------+
|to_port                   |xsd:int *(Required)*     |The port at end of range.|
+--------------------------+-------------------------+-------------------------+
|ip_range                  |xsd:dict *(Required)*    |An ``ip_range`` object.  |
+--------------------------+-------------------------+-------------------------+
|cidr                      |xsd:string *(Required)*  |The CIDR for address     |
|                          |                         |range.                   |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The security group ID.   |
+--------------------------+-------------------------+-------------------------+
|group                     |xsd:dict *(Required)*    |A ``group`` object.      |
|                          |                         |Includes the tenant ID   |
|                          |                         |and the source security  |
|                          |                         |group name.              |
+--------------------------+-------------------------+-------------------------+
|parent_group_id           |csapi:UUID *(Required)*  |Security group ID.       |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The source security      |
|                          |                         |group name.              |
+--------------------------+-------------------------+-------------------------+





**Example Create security group rule: JSON response**


.. code::

    {
        "security_group_rule": {
            "id": "1",
            "ip_range": {
                "cidr": "0.0.0.0/0"
            },
            "parent_group_id": "48700ff3-30b8-4e63-845f-a79c9633e9fb",
            "to_port": 443,
            "ip_protocol": "tcp",
            "group": {},
            "from_port": 443
        }
    }
    

