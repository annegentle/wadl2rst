=============================================================================
List Security Groups -  OpenStack Compute API v2.1
=============================================================================

List Security Groups
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_security_groups_v2.1_tenant_id_os-security-groups.rst#request>`__
`Response <GET_list_security_groups_v2.1_tenant_id_os-security-groups.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-security-groups

Lists security groups.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |List security groups:    |                         |
|                          |JSON response            |                         |
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
    

