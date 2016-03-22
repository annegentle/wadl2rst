=============================================================================
Delete Dns Entry -  OpenStack Compute API v2.1
=============================================================================

Delete Dns Entry
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_dns_entry_v2.1_tenant_id_os-floating-ip-dns_domain_entries_name_.rst#request>`__
`Response <DELETE_delete_dns_entry_v2.1_tenant_id_os-floating-ip-dns_domain_entries_name_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{name}

Deletes a DNS entry.



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
|{domain}                  |xsd:string *(Required)*  |The registered DNS       |
|                          |                         |domain that the DNS      |
|                          |                         |drivers publish.         |
+--------------------------+-------------------------+-------------------------+
|{name}                    |xsd:string               |The name of the DNS      |
|                          |                         |entry.                   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




