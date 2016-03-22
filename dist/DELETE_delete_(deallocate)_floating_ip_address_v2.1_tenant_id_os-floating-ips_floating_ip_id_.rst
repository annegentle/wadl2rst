=============================================================================
Delete (Deallocate) Floating Ip Address -  OpenStack Compute API v2.1
=============================================================================

Delete (Deallocate) Floating Ip Address
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_(deallocate)_floating_ip_address_v2.1_tenant_id_os-floating-ips_floating_ip_id_.rst#request>`__
`Response <DELETE_delete_(deallocate)_floating_ip_address_v2.1_tenant_id_os-floating-ips_floating_ip_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-floating-ips/{floating_ip_id}

Deletes, or deallocates, a floating IP address from the current project and returns it to the pool from which it was allocated.

If the IP address is still associated with a running instance, it is automatically disassociated from that instance.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
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
|{floating_ip_id}          |xsd:int                  |The ID of the floating   |
|                          |                         |IP address.              |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




