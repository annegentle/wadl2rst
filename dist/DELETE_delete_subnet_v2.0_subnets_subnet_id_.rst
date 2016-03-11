=============================================================================
Delete Subnet -  OpenStack Compute API v2.1
=============================================================================

Delete Subnet
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_subnet_v2.0_subnets_subnet_id_.rst#request>`__
`Response <DELETE_delete_subnet_v2.0_subnets_subnet_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/subnets/{subnet_id}

Deletes a subnet.

The operation fails if subnet IP addresses are still allocated.



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
|{subnet_id}               |csapi:UUID               |The UUID of the subnet.  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




