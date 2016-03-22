=============================================================================
List Server Groups -  OpenStack Compute API v2.1
=============================================================================

List Server Groups
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_server_groups_v2.1_tenant_id_os-server-groups.rst#request>`__
`Response <GET_list_server_groups_v2.1_tenant_id_os-server-groups.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-server-groups

Lists all server groups for the tenant.

Administrative users can use the ``all_projects`` query parameter to list all server groups for all projects.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+-----------------------+-----------------------+------------------------------+
|Name                   |Type                   |Description                   |
+=======================+=======================+==============================+
|all_projects           |xsd:boolean            |Administrator only. Lists     |
|                       |*(Required)*           |server groups for all         |
|                       |                       |projects. For example: GET    |
|                       |                       |/v2.1/​{admin_tenant_id}​/os- |
|                       |                       |server-                       |
|                       |                       |groups?all_projects=TrueIf    |
|                       |                       |you specify a tenant ID for a |
|                       |                       |non-administrative user with  |
|                       |                       |this query parameter, the     |
|                       |                       |call lists all server groups  |
|                       |                       |for the tenant, or project,   |
|                       |                       |rather than for all projects. |
+-----------------------+-----------------------+------------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|server_groups             |xsd:dict *(Required)*    |A ``server_groups``      |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the server   |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name of the server   |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|policies                  |xsd:dict *(Required)*    |A list of policies for   |
|                          |                         |the server group.        |
+--------------------------+-------------------------+-------------------------+
|members                   |xsd:dict *(Required)*    |A list of members in the |
|                          |                         |server group.            |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:string *(Required)*  |A dictionary of metadata |
|                          |                         |key-and-value pairs,     |
|                          |                         |which is maintained for  |
|                          |                         |backward compatibility.  |
|                          |                         |The API always returns   |
|                          |                         |an empty metadata        |
|                          |                         |dictionary.              |
+--------------------------+-------------------------+-------------------------+





**Example List Server Groups: JSON request**


.. code::

    {
        "server_groups": [
            {
                "id": "616fb98f-46ca-475e-917e-2563e5a8cd19",
                "name": "test",
                "policies": [
                    "anti-affinity"
                ],
                "members": [],
                "metadata": {}
            }
        ]
    }
    

