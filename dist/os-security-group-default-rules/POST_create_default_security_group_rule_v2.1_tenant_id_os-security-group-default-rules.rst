
Create Default Security Group Rule
==================================

.. rest_method:: POST /v2.1/{tenant_id}/os-security-group-default-rules

Creates a default security group rule.

If you specify a source port ( ``from_port`` ) or destination port ( ``to_port`` ) value, you must specify an IP protocol ( ``ip_protocol`` ) value. Otherwise, the operation returns the ``Bad Request (400)`` response code.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createDefaultSecurityGroupRule.yaml

	- tenant_id: tenant_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../createDefaultSecurityGroupRule.yaml

	- id: id
	- ip_protocol: ip_protocol
	- from_port: from_port
	- to_port: to_port
	- cidr: cidr




**Example Create default security group rule: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-security-group-default-rules/security-group-default-rule-create-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../createDefaultSecurityGroupRule.yaml

	- from_port: from_port
	- id: id
	- ip_protocol: ip_protocol
	- ip_range: ip_range
	- cidr: cidr
	- to_port: to_port




**Example Create default security group rule: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-security-group-default-rules/security-group-default-rule-create-resp.json
   :language: javascript


