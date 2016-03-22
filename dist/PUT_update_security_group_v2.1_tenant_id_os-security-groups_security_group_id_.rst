=============================================================================
Update Security Group -  OpenStack Compute API v2.1
=============================================================================

Update Security Group
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_security_group_v2.1_tenant_id_os-security-groups_security_group_id_.rst#request>`__
`Response <PUT_update_security_group_v2.1_tenant_id_os-security-groups_security_group_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/os-security-groups/{security_group_id}

Updates a security group.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Update security group:   |                         |
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
|{security_group_id}       |xsd:int                  |The ID of the security   |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The security group name. |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Security group           |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+





**Example Update security group: JSON request**


.. code::

    {
        "security_group": {
            "name": "mysecgroup",
            "description": "my security group"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^


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
|rules                     |xsd:dict *(Required)*    |A security group rules   |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |xsd:string *(Required)*  |The tenant ID.           |
+--------------------------+-------------------------+-------------------------+





**Example Update security group: JSON response**


.. code::

    {
        "security_group": {
            "description": "my security group",
            "id": 1,
            "name": "mysecgroup",
            "rules": [],
            "tenant_id": "a52cdb9cc7854a39a23d3af73a40899e"
        }
    }
    

