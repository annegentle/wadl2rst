
Show Floating Ip Address Details
================================

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ips/{floating_ip_id}

Shows details for a floating IP address, by ID, that is associated with the tenant or account.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showFloatingIpAddressDetails.yaml

	- tenant_id: tenant_id
	- floating_ip_id: floating_ip_id








Response
^^^^^^^^





**Example Show Floating Ip Address Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips/floating-ip-show-resp.json
   :language: javascript


