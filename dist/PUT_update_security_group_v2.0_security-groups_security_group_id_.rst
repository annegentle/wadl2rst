=============================================================================
Update Security Group -  OpenStack Compute API v2.1
=============================================================================

Update Security Group
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_security_group_v2.0_security-groups_security_group_id_.rst#request>`__
`Response <PUT_update_security_group_v2.0_security-groups_security_group_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/security-groups/{security_group_id}

Updates a security group.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Update security group:   |                         |
|                          |JSON response            |                         |
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|413                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{security_group_id}       |csapi:UUID *(Required)*  |The UUID of the security |
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

    {"security_group": {"name": "mysecgroup","description": "my security group"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group            |xsd:dict *(Required)*    |A ``security_group``     |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The security group       |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the security |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The security group name. |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |xsd:string *(Required)*  |The UUID of the tenant.  |
+--------------------------+-------------------------+-------------------------+





**Example Update security group: JSON response**


.. code::

    {"security_group": {"rules": [],"tenant_id": "a52cdb9cc7854a39a23d3af73a40899e","id": "01fbade5-b664-42f6-83ae-4e214f4263fa","name": "mysecgroup","description": "my security group"}}

