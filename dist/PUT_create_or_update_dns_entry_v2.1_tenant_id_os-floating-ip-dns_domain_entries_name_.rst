=============================================================================
Create Or Update Dns Entry -  OpenStack Compute API v2.1
=============================================================================

Create Or Update Dns Entry
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_create_or_update_dns_entry_v2.1_tenant_id_os-floating-ip-dns_domain_entries_name_.rst#request>`__
`Response <PUT_create_or_update_dns_entry_v2.1_tenant_id_os-floating-ip-dns_domain_entries_name_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{name}

Creates or updates a DNS entry.



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








**Example Create Or Update Dns Entry: JSON request**


.. code::

    {
        "dns_entry": {
            "ip": "192.168.53.11",
            "dns_type": "A"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Or Update Dns Entry: JSON request**


.. code::

    {
        "dns_entry": {
            "domain": "domain1.example.org",
            "id": null,
            "ip": "192.168.1.1",
            "name": "instance1",
            "type": "A"
        }
    }
    

