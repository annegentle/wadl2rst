
Create (Allocate) Floating Ip Address
=====================================

.. rest_method:: POST /v2.1/{tenant_id}/os-floating-ips

Creates, or allocates, a floating IP address for the current project. By default, the floating IP address is allocated from the public pool.

If more than one floating IP address pool is available, use the ``pool`` parameter to specify from which pool to allocate the IP address.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200,400

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../create(Allocate)FloatingIpAddress.yaml

	- tenant_id: tenant_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../create(Allocate)FloatingIpAddress.yaml

	- pool: pool




**Example Create (Allocate) Floating Ip Address: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips/floating-ip-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create (Allocate) Floating Ip Address: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips/floating-ip-create-resp.json
   :language: javascript


