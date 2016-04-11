
List Security Groups
====================

.. rest_method:: GET /v2.1/{tenant_id}/os-security-groups

Lists security groups.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listSecurityGroups.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^


.. rest_parameters:: ../listSecurityGroups.yaml

	- security_groups: security_groups
	- description: description
	- id: id
	- name: name
	- rules: rules
	- tenant_id: tenant_id




**Example List security groups: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-security-groups/security-groups-list-resp.json
   :language: javascript


