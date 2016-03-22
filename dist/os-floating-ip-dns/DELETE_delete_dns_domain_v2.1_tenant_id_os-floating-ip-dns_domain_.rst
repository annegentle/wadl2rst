=============================================================================
Delete Dns Domain -  OpenStack Compute API v2.1
=============================================================================

Delete Dns Domain
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_dns_domain_v2.1_tenant_id_os-floating-ip-dns_domain_.rst#request>`__
`Response <DELETE_delete_dns_domain_v2.1_tenant_id_os-floating-ip-dns_domain_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.1/{tenant_id}/os-floating-ip-dns/{domain}

Deletes a DNS domain and all associated host entries.



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








Response
^^^^^^^^^^^^^^^^^^




