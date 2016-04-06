
List Dns Domains
================

`Request <GET_list_dns_domains_v2.1_tenant_id_os-floating-ip-dns.rst#request>`__
`Response <GET_list_dns_domains_v2.1_tenant_id_os-floating-ip-dns.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ip-dns

Lists registered DNS domains published by the DNS drivers.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





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
    

