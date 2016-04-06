
List Default Security Group Rules
=================================

`Request <GET_list_default_security_group_rules_v2.1_tenant_id_os-security-group-default-rules.rst#request>`__
`Response <GET_list_default_security_group_rules_v2.1_tenant_id_os-security-group-default-rules.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-security-group-default-rules

Lists default security group rules.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^


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
|ip_range                  |xsd:dict *(Required)*    |An IP range object.      |
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
    

