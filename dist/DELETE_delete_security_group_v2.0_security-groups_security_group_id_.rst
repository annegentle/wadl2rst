=============================================================================
Delete Security Group -  OpenStack Compute API v2.1
=============================================================================

Delete Security Group
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_security_group_v2.0_security-groups_security_group_id_.rst#request>`__
`Response <DELETE_delete_security_group_v2.0_security-groups_security_group_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/security-groups/{security_group_id}

Deletes an OpenStack Networking security group.

This operation deletes an OpenStack Networking security group and its associated security group rules, provided that a port is not associated with the security group.

This operation does not require a request body. This operation does not return a response body.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
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








**Example Delete Security Group: JSON request**


.. code::

    DELETE /v2.0/security-groups/e470bdfc-4869-459b-a561-cb3377efae59Content-Type: application/jsonAccept: application/json


Response
^^^^^^^^^^^^^^^^^^





**Example Delete Security Group: JSON request**


.. code::

    status: 204

