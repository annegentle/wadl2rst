
Create Or Update Dns Entry
==========================

`Request <PUT_create_or_update_dns_entry_v2.1_tenant_id_os-floating-ip-dns_domain_entries_name_.rst#request>`__
`Response <PUT_create_or_update_dns_entry_v2.1_tenant_id_os-floating-ip-dns_domain_entries_name_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{name}

Creates or updates a DNS entry.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Create Or Update Dns Entry: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ip-dns/floating-ip-dns-create-or-update-entry-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Or Update Dns Entry: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ip-dns/floating-ip-dns-create-or-update-entry-resp.json
   :language: javascript

