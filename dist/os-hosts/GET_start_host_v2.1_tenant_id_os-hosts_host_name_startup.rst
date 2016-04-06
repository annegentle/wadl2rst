
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

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- host_name: host_name







Response
^^^^^^^^





**Example Start Host: JSON request**


.. code::

    {
        "host": "4b392b27930343bbaa27fd5d8328a564",
        "power_action": "startup"
    }
    

