
Create Or Update Dns Domain
===========================

`Request <PUT_create_or_update_dns_domain_v2.1_tenant_id_os-floating-ip-dns_domain_.rst#request>`__
`Response <PUT_create_or_update_dns_domain_v2.1_tenant_id_os-floating-ip-dns_domain_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-floating-ip-dns/{domain}

Creates or updates a DNS domain.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- domain: domain







**Example Create Or Update Dns Domain: JSON request**


.. code::

    {
        "domain_entry": {
            "scope": "public",
            "project": "project1"
        }
    }
    


Response
^^^^^^^^





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
    

