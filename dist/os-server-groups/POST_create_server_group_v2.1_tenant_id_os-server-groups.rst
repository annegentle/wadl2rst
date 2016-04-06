
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The server group name. A |
|                          |                         |non-empty string with no |
|                          |                         |leading or trailing      |
|                          |                         |spaces. Maximum length   |
|                          |                         |is 255 characters.       |
+--------------------------+-------------------------+-------------------------+
|policies                  |xsd:list *(Required)*    |A list of one or more    |
|                          |                         |policy names to          |
|                          |                         |associate with the       |
|                          |                         |server group. The list   |
|                          |                         |must contain at least    |
|                          |                         |one policy name. The     |
|                          |                         |current valid policy     |
|                          |                         |names are ``anti-        |
|                          |                         |affinity`` and           |
|                          |                         |``affinity``. Each       |
|                          |                         |policy name must be a    |
|                          |                         |non-empty string with no |
|                          |                         |leading or trailing      |
|                          |                         |spaces. Maximum length   |
|                          |                         |is 255 characters.       |
+--------------------------+-------------------------+-------------------------+





**Example Create Server Group: JSON request**


.. code::

    {
        "server_group": {
            "name": "test",
            "policies": [
                "anti-affinity"
            ]
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





**Example Create Server Group: JSON request**


.. code::

    {
        "server_group": {
            "id": "5bbcc3c4-1da2-4437-a48a-66f15b1b13f9",
            "name": "test",
            "policies": [
                "anti-affinity"
            ],
            "members": [],
            "metadata": {}
        }
    }
    

