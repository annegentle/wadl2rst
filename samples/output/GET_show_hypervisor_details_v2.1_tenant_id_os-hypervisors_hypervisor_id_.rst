=============================================================================
Show Hypervisor Details -  OpenStack Compute API v2.1
=============================================================================

Show Hypervisor Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_hypervisor_details_v2.1_tenant_id_os-hypervisors_hypervisor_id_.rst#request>`__
`Response <GET_show_hypervisor_details_v2.1_tenant_id_os-hypervisors_hypervisor_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-hypervisors/{hypervisor_id}

Shows details for a hypervisor.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{hypervisor_id}           |csapi:UUID               |The UUID of the          |
|                          |                         |hypervisor.              |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Hypervisor Details: JSON request**


.. code::

    {
        "hypervisor": {
            "status": "enabled",
            "service": {
                "host": "fake-mini",
                "disabled_reason": null,
                "id": 6
            },
            "vcpus_used": 0,
            "hypervisor_type": "QEMU",
            "local_gb_used": 0,
            "vcpus": 8,
            "hypervisor_hostname": "fake-mini",
            "memory_mb_used": 512,
            "memory_mb": 7980,
            "current_workload": 0,
            "state": "up",
            "host_ip": "23.253.248.171",
            "cpu_info": "{\"vendor\": \"Intel\", \"model\": \"gate64\", \"arch\": \"x86_64\", \"features\": [\"pge\", \"clflush\", \"sep\", \"syscall\", \"vme\", \"msr\", \"cmov\", \"fpu\", \"pat\", \"lm\", \"tsc\", \"nx\", \"fxsr\", \"sse4.1\", \"pae\", \"sse4.2\", \"pclmuldq\", \"tsc-deadline\", \"mmx\", \"cx8\", \"mce\", \"de\", \"rdtscp\", \"mca\", \"pse\", \"pni\", \"popcnt\", \"apic\", \"sse\", \"lahf_lm\", \"aes\", \"sse2\", \"hypervisor\", \"ssse3\", \"cx16\", \"mtrr\", \"x2apic\"], \"topology\": {\"cores\": 1, \"cells\": 1, \"threads\": 1, \"sockets\": 8}}",
            "running_vms": 0,
            "free_disk_gb": 157,
            "hypervisor_version": 2000000,
            "disk_available_least": 140,
            "local_gb": 157,
            "free_ram_mb": 7468,
            "id": 1
        }
    }
    

