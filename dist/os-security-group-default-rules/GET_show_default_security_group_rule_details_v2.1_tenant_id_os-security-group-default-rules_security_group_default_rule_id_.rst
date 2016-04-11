
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







Response
^^^^^^^^


.. rest_parameters:: ../showDefaultSecurityGroupRuleDetails.yaml

	- from_port: from_port
	- id: id
	- ip_protocol: ip_protocol
	- ip_range: ip_range
	- cidr: cidr
	- to_port: to_port




**Example Show default security group rule: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-security-group-default-rules/security-group-default-rule-show-resp.json
   :language: javascript

