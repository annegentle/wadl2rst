
Show Security Group Details
===========================

`Request <GET_show_security_group_details_v2.1_tenant_id_os-security-groups_security_group_id_.rst#request>`__
`Response <GET_show_security_group_details_v2.1_tenant_id_os-security-groups_security_group_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-security-groups/{security_group_id}

Shows details for a security group.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: showSecurityGroupDetails.yaml

	- security_group: security_group
	- description: description
	- id: id
	- name: name
	- rules: rules
	- tenant_id: tenant_id




**Example Show security group: JSON response**


.. code::

    {
        "security_group": {
            "description": "default",
            "id": 1,
            "name": "default",
            "rules": [],
            "tenant_id": "openstack"
        }
    }
    

