
Delete Dns Domain
=================

.. rest_method:: DELETE /v2.1/{tenant_id}/os-floating-ip-dns/{domain}

Deletes a DNS domain and all associated host entries.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteDnsDomain.yaml

	- tenant_id: tenant_id
	- domain: domain








Response
^^^^^^^^




