
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group            |xsd:string *(Required)*  |Specify the              |
|                          |                         |``security_group``       |
|                          |                         |action in the request    |
|                          |                         |body.                    |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The security group name. |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Security group           |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+





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


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group            |xsd:string *(Required)*  |Security group object.   |
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
    

