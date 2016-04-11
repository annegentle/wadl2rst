
List Security Groups By Server
==============================

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-security-groups

Lists security groups for a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listSecurityGroupsByServer.yaml

	- tenant_id: tenant_id
	- server_id: server_id








Response
^^^^^^^^


.. rest_parameters:: ../listSecurityGroupsByServer.yaml

	- security_groups: security_groups
	- description: description
	- id: id
	- name: name
	- rules: rules
	- tenant_id: tenant_id




**Example List security groups by server: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-security-groups/security-groups-list-resp.json
   :language: javascript


