
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







Response
^^^^^^^^


.. rest_parameters:: ../listDefaultSecurityGroupRules.yaml

	- from_port: from_port
	- id: id
	- ip_protocol: ip_protocol
	- ip_range: ip_range
	- cidr: cidr
	- to_port: to_port




**Example List default security group rules: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-security-group-default-rules/security-group-default-rules-list-resp.json
   :language: javascript

