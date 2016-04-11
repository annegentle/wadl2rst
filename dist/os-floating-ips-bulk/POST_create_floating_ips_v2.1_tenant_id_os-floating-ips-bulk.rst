
Create Floating Ips
===================

.. rest_method:: POST /v2.1/{tenant_id}/os-floating-ips-bulk

Bulk-creates floating IPs.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createFloatingIps.yaml

	- tenant_id: tenant_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../createFloatingIps.yaml

	- ip_range: ip_range




**Example Create Floating Ips: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips-bulk/floating-ips-bulk-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Floating Ips: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips-bulk/floating-ips-bulk-create-resp.json
   :language: javascript


