
Enable Host
===========

`Request <PUT_enable_host_v2.1_tenant_id_os-hosts_host_name_.rst#request>`__
`Response <PUT_enable_host_v2.1_tenant_id_os-hosts_host_name_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/os-hosts/{host_name}

Enables or puts a host in maintenance mode.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







**Example Enable Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-update-maintenance-req.json
   :language: javascript



Response
^^^^^^^^





**Example Enable Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-update-maintenance-resp.json
   :language: javascript

