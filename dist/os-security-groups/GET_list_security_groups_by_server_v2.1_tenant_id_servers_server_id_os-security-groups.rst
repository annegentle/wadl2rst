=============================================================================
List Security Groups By Server -  OpenStack Compute API v2.1
=============================================================================

List Security Groups By Server
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_security_groups_by_server_v2.1_tenant_id_servers_server_id_os-security-groups.rst#request>`__
`Response <GET_list_security_groups_by_server_v2.1_tenant_id_servers_server_id_os-security-groups.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/os-security-groups

Lists security groups for a server.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |List security groups by  |Security groups object.  |
|                          |server: JSON response    |The security group       |
|                          |                         |description. The ID of   |
|                          |                         |the security group. The  |
|                          |                         |security group name. A   |
|                          |                         |security group rules     |
|                          |                         |object. The tenant ID.   |
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
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_groups           |xsd:string *(Required)*  |Security groups object.  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The security group       |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+
|id                        |xsd:int *(Required)*     |The ID of the security   |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The security group name. |
+--------------------------+-------------------------+-------------------------+
|rules                     |xsd:dict *(Required)*    |A security group rules   |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |xsd:string *(Required)*  |The tenant ID.           |
+--------------------------+-------------------------+-------------------------+





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
    

