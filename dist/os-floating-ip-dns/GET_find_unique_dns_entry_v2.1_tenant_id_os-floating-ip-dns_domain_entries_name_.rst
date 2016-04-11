
Find Unique Dns Entry
=====================

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ip-dns/{domain}/entries/{name}

Finds a unique DNS entry for a domain and name.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../findUniqueDnsEntry.yaml

	- tenant_id: tenant_id
	- domain: domain
	- name: name








Response
^^^^^^^^





**Example Find Unique Dns Entry: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ip-dns/floating-ip-dns-entry-show-resp.json
   :language: javascript


