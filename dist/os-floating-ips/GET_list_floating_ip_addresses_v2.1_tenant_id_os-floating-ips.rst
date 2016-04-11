
List Floating Ip Addresses
==========================

`Request <GET_list_floating_ip_addresses_v2.1_tenant_id_os-floating-ips.rst#request>`__
`Response <GET_list_floating_ip_addresses_v2.1_tenant_id_os-floating-ips.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-floating-ips

Lists floating IP addresses associated with the tenant or account.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example List Floating Ip Addresses: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-floating-ips/floating-ips-list-resp.json
   :language: javascript

