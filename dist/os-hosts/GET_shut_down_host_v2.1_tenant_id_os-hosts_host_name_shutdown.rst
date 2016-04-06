
Shut Down Host
==============

`Request <GET_shut_down_host_v2.1_tenant_id_os-hosts_host_name_shutdown.rst#request>`__
`Response <GET_shut_down_host_v2.1_tenant_id_os-hosts_host_name_shutdown.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-hosts/{host_name}/shutdown

Shuts down a host.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- host_name: host_name







Response
^^^^^^^^





**Example Shut Down Host: JSON request**


.. code::

    {
        "host": "77cfa0002e4d45fe97f185968111b27b",
        "power_action": "shutdown"
    }
    

