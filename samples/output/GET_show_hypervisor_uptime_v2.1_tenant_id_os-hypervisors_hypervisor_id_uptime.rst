=============================================================================
Show Hypervisor Uptime -  OpenStack Compute API v2.1
=============================================================================

Show Hypervisor Uptime
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_hypervisor_uptime_v2.1_tenant_id_os-hypervisors_hypervisor_id_uptime.rst#request>`__
`Response <GET_show_hypervisor_uptime_v2.1_tenant_id_os-hypervisors_hypervisor_id_uptime.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-hypervisors/{hypervisor_id}/uptime

Shows the uptime for a hypervisor.



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
    

