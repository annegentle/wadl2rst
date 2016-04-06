
List Dns Entries
================

`Request <GET_list_dns_entries_v2.1_tenant_id_os-floating-ip-dns_domain_entries_ip_.rst#request>`__
`Response <GET_list_dns_entries_v2.1_tenant_id_os-floating-ip-dns_domain_entries_ip_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{ip}

Lists DNS entries for a domain and IP.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- domain: domain
	- ip: ip







Response
^^^^^^^^





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
    

