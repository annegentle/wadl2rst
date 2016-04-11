
Show Security Group Details
===========================

.. rest_method:: GET /v2.1/{tenant_id}/os-security-groups/{security_group_id}

Shows details for a security group.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showSecurityGroupDetails.yaml

	- tenant_id: tenant_id
	- security_group_id: security_group_id








Response
^^^^^^^^


.. rest_parameters:: ../showSecurityGroupDetails.yaml

	- security_group: security_group
	- description: description
	- id: id
	- name: name
	- rules: rules
	- tenant_id: tenant_id




**Example Show security group: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-security-groups/security-group-show-resp.json
   :language: javascript


