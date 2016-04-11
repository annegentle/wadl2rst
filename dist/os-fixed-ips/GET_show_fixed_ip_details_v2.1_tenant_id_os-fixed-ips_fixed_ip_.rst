
Show Fixed Ip Details
=====================

.. rest_method:: GET /v2.1/{tenant_id}/os-fixed-ips/{fixed_ip}

Shows details for a fixed IP address.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showFixedIpDetails.yaml

	- tenant_id: tenant_id
	- fixed_ip: fixed_ip








Response
^^^^^^^^





**Example Show Fixed Ip Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-fixed-ips/fixedip-show-resp.json
   :language: javascript


