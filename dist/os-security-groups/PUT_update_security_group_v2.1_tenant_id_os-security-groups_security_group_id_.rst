
Update Security Group
=====================

.. rest_method:: PUT /v2.1/{tenant_id}/os-security-groups/{security_group_id}

Updates a security group.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../updateSecurityGroup.yaml

	- tenant_id: tenant_id
	- security_group_id: security_group_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../updateSecurityGroup.yaml

	- name: name
	- description: description




**Example Update security group: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-security-groups/security-group-update-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../updateSecurityGroup.yaml

	- security_group: security_group
	- description: description
	- id: id
	- name: name
	- rules: rules
	- tenant_id: tenant_id




**Example Update security group: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-security-groups/security-group-update-resp.json
   :language: javascript


