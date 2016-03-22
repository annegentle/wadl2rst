=============================================================================
Create Or Update Dns Domain -  OpenStack Compute API v2.1
=============================================================================

Create Or Update Dns Domain
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_create_or_update_dns_domain_v2.1_tenant_id_os-floating-ip-dns_domain_.rst#request>`__
`Response <PUT_create_or_update_dns_domain_v2.1_tenant_id_os-floating-ip-dns_domain_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/os-floating-ip-dns/{domain}

Creates or updates a DNS domain.



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








**Example Create Or Update Dns Domain: JSON request**


.. code::

    {
        "domain_entry": {
            "scope": "public",
            "project": "project1"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Or Update Dns Domain: JSON request**


.. code::

    {
        "domain_entry": {
            "availability_zone": null,
            "domain": "domain1.example.org",
            "project": "project1",
            "scope": "public"
        }
    }
    

