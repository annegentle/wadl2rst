
List Dns Domains
================

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ip-dns

Lists registered DNS domains published by the DNS drivers.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listDnsDomains.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example List Dns Domains: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ip-dns/floating-ip-dns-domains-list-resp.json
   :language: javascript


