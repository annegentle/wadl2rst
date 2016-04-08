
List Security Groups By Server
==============================

`Request <GET_list_security_groups_by_server_v2.1_tenant_id_servers_server_id_os-security-groups.rst#request>`__
`Response <GET_list_security_groups_by_server_v2.1_tenant_id_servers_server_id_os-security-groups.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-security-groups

Lists security groups for a server.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: listSecurityGroupsByServer.yaml

	- security_groups: security_groups
	- description: description
	- id: id
	- name: name
	- rules: rules
	- tenant_id: tenant_id




**Example List security groups by server: JSON response**


.. code::

    {
        "security_groups": [
            {
                "description": "default",
                "id": 1,
                "name": "default",
                "rules": [],
                "tenant_id": "openstack"
            }
        ]
    }
    

