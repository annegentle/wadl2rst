
Create Server Group
===================

`Request <POST_create_server_group_v2.1_tenant_id_os-server-groups.rst#request>`__
`Response <POST_create_server_group_v2.1_tenant_id_os-server-groups.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-server-groups

Creates a server group.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../createServerGroup.yaml

	- name: name
	- policies: policies




**Example Create Server Group: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-server-groups/server-group-create-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../createServerGroup.yaml

	- server_groups: server_groups
	- id: id
	- name: name
	- policies: policies
	- members: members
	- metadata: metadata
	- project_id: project_id
	- user_id: user_id




**Example Create Server Group: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-server-groups/server-group-create-resp.json
   :language: javascript

