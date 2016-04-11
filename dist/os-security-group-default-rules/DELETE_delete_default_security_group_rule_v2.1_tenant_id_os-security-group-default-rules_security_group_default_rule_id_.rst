
Delete Default Security Group Rule
==================================

.. rest_method:: DELETE /v2.1/{tenant_id}/os-security-group-default-rules/{security_group_default_rule_id}

Deletes a security group rule.



Normal response codes: 204,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteDefaultSecurityGroupRule.yaml

	- tenant_id: tenant_id
	- security_group_default_rule_id: security_group_default_rule_id








Response
^^^^^^^^




