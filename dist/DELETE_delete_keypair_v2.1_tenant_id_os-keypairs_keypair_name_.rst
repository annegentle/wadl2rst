=============================================================================
Delete Keypair -  OpenStack Compute API v2.1
=============================================================================

Delete Keypair
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_keypair_v2.1_tenant_id_os-keypairs_keypair_name_.rst#request>`__
`Response <DELETE_delete_keypair_v2.1_tenant_id_os-keypairs_keypair_name_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-keypairs/{keypair_name}

Deletes a keypair.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{keypair_name}            |xsd:string               |The keypair name.        |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




