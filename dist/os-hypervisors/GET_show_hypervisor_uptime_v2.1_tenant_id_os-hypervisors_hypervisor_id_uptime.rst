
Show Hypervisor Uptime
======================

`Request <GET_show_hypervisor_uptime_v2.1_tenant_id_os-hypervisors_hypervisor_id_uptime.rst#request>`__
`Response <GET_show_hypervisor_uptime_v2.1_tenant_id_os-hypervisors_hypervisor_id_uptime.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-hypervisors/{hypervisor_id}/uptime

Shows the uptime for a hypervisor.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- hypervisor_id: hypervisor_id







Response
^^^^^^^^





**Example Show Hypervisor Uptime: JSON request**


.. code::

    {
        "hypervisor": {
            "status": "enabled",
            "state": "up",
            "id": 1,
            "hypervisor_hostname": "fake-mini",
            "uptime": " 16:09:43 up 8 days, 19:58,  1 user,  load average: 0.86, 0.63, 0.55\n"
        }
    }
    

