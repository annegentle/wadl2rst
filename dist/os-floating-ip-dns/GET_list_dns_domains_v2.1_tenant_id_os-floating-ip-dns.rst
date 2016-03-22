=============================================================================
List Dns Domains -  OpenStack Compute API v2.1
=============================================================================

List Dns Domains
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_dns_domains_v2.1_tenant_id_os-floating-ip-dns.rst#request>`__
`Response <GET_list_dns_domains_v2.1_tenant_id_os-floating-ip-dns.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-floating-ip-dns

Lists registered DNS domains published by the DNS drivers.



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








Response
^^^^^^^^^^^^^^^^^^





**Example List Dns Domains: JSON request**


.. code::

    {
        "domain_entries": [
            {
                "availability_zone": null,
                "domain": "domain1.example.org",
                "project": "project1",
                "scope": "public"
            }
        ]
    }
    

