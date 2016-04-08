
Show Hypervisor Statistics
==========================

`Request <GET_show_hypervisor_statistics_v2.1_tenant_id_os-hypervisors_statistics.rst#request>`__
`Response <GET_show_hypervisor_statistics_v2.1_tenant_id_os-hypervisors_statistics.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-hypervisors/statistics

Shows summary statistics for all hypervisors over all compute nodes.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Hypervisor Statistics: JSON request**


.. code::

    {
        "hypervisor_statistics": {
            "count": 1,
            "vcpus_used": 0,
            "local_gb_used": 0,
            "memory_mb": 7980,
            "current_workload": 0,
            "vcpus": 8,
            "running_vms": 0,
            "free_disk_gb": 157,
            "disk_available_least": 140,
            "local_gb": 157,
            "free_ram_mb": 7468,
            "memory_mb_used": 512
        }
    }
    

