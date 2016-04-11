
Reboot Host
===========

`Request <GET_reboot_host_v2.1_tenant_id_os-hosts_host_name_reboot.rst#request>`__
`Response <GET_reboot_host_v2.1_tenant_id_os-hosts_host_name_reboot.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/reboot

Reboots a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Reboot Host: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-hosts/host-reboot-resp.json
   :language: javascript

