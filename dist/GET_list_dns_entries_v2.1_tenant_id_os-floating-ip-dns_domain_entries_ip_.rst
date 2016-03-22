=============================================================================
List Dns Entries -  OpenStack Compute API v2.1
=============================================================================

List Dns Entries
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_dns_entries_v2.1_tenant_id_os-floating-ip-dns_domain_entries_ip_.rst#request>`__
`Response <GET_list_dns_entries_v2.1_tenant_id_os-floating-ip-dns_domain_entries_ip_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{ip}

Lists DNS entries for a domain and IP.



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
|{ip}                      |xsd:string               |The IP address.          |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Dns Entries: JSON request**


.. code::

    {
        "dns_entries": [
            {
                "domain": "domain1.example.org",
                "id": null,
                "ip": "192.168.1.1",
                "name": "instance1",
                "type": null
            }
        ]
    }
    

