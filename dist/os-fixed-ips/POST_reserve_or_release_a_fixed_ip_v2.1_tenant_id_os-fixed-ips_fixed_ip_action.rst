
Reserve Or Release A Fixed Ip
=============================

.. rest_method:: POST /v2.1/{tenant_id}/os-fixed-ips/{fixed_ip}/action

Reserves or releases a fixed IP.

To reserve a fixed IP address, specify ``reserve`` in the request body. To release a fixed IP address, specify ``unreserve`` in the request body.



Normal response codes: 202,,503,400,401,403,405,415,400

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../reserveOrReleaseAFixedIp.yaml

	- tenant_id: tenant_id
	- fixed_ip: fixed_ip








**Example Reserve Or Release A Fixed Ip: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-fixed-ips/fixedip-create-req.json
   :language: javascript



Response
^^^^^^^^




