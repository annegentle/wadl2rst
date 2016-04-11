
List Server Groups
==================

`Request <GET_list_server_groups_v2.1_tenant_id_os-server-groups.rst#request>`__
`Response <GET_list_server_groups_v2.1_tenant_id_os-server-groups.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-server-groups

Lists all server groups for the tenant.

Administrative users can use the ``all_projects`` query parameter to list all server groups for all projects.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: ../listServerGroups.yaml

	- all_projects: all_projects






Response
^^^^^^^^


.. rest_parameters:: ../listServerGroups.yaml

	- server_groups: server_groups
	- id: id
	- name: name
	- policies: policies
	- members: members
	- metadata: metadata
	- project_id: project_id
	- user_id: user_id




**Example List Server Groups: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-server-groups/server-groups-list-resp.json
   :language: javascript

