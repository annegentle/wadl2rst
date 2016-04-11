
List Dns Entries
================

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{ip}

Lists DNS entries for a domain and IP.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listDnsEntries.yaml

	- tenant_id: tenant_id
	- domain: domain
	- ip: ip








Response
^^^^^^^^





**Example List Dns Entries: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ip-dns/floating-ip-dns-entry-by-ip-show-resp.json
   :language: javascript


