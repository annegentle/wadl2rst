
Start Host
==========

`Request <GET_start_host_v2.1_tenant_id_os-hosts_host_name_startup.rst#request>`__
`Response <GET_start_host_v2.1_tenant_id_os-hosts_host_name_startup.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/startup

Starts a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Start Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-start-resp.json
   :language: javascript

