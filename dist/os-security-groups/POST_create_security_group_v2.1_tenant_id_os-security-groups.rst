
Create Security Group
=====================

`Request <POST_create_security_group_v2.1_tenant_id_os-security-groups.rst#request>`__
`Response <POST_create_security_group_v2.1_tenant_id_os-security-groups.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-security-groups

Creates a security group.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: createSecurityGroup.yaml

	- security_group: security_group
	- name: name
	- description: description




**Example Create security group: JSON request**


.. code::

    {
        "security_group": {
            "name": "test",
            "description": "description"
        }
    }
    


Response
^^^^^^^^


.. rest_parameters:: createSecurityGroup.yaml

	- security_group: security_group
	- description: description
	- id: id
	- name: name
	- rules: rules
	- tenant_id: tenant_id




**Example Create security group: JSON response**


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
    

