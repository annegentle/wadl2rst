=============================================================================
Delete Port -  OpenStack Compute API v2.1
=============================================================================

Delete Port
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_port_v2.0_ports_port_id_.rst#request>`__
`Response <DELETE_delete_port_v2.0_ports_port_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/ports/{port_id}

Deletes a port.

Any IP addresses that are associated with the port are returned to the respective subnets allocation pools.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{port_id}                 |csapi:UUID *(Required)*  |The UUID of the port.    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




