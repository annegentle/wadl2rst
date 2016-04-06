
List Security Groups
====================

`Request <GET_list_security_groups_v2.1_tenant_id_os-security-groups.rst#request>`__
`Response <GET_list_security_groups_v2.1_tenant_id_os-security-groups.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-security-groups

Lists security groups.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_groups           |xsd:list *(Required)*    |Security groups object.  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The security group       |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+
|id                        |xsd:int *(Required)*     |The ID of the security   |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The security group name. |
+--------------------------+-------------------------+-------------------------+
|rules                     |xsd:list *(Required)*    |A security group rules   |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |xsd:string *(Required)*  |The tenant ID.           |
+--------------------------+-------------------------+-------------------------+





**Example List security groups: JSON response**


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
    

