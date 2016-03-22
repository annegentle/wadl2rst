=============================================================================
Show Host Details -  OpenStack Compute API v2.1
=============================================================================

Show Host Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_host_details_v2.1_tenant_id_os-hosts_host_name_.rst#request>`__
`Response <GET_show_host_details_v2.1_tenant_id_os-hosts_host_name_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-hosts/{host_name}

Shows details for a host.



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
|{host_name}               |xsd:string               |The name of the host.    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Host Details: JSON request**


.. code::

    {
        "host": [
            {
                "resource": {
                    "cpu": 1,
                    "disk_gb": 1028,
                    "host": "c1a7de0ac9d94e4baceae031d05caae3",
                    "memory_mb": 8192,
                    "project": "(total)"
                }
            },
            {
                "resource": {
                    "cpu": 0,
                    "disk_gb": 0,
                    "host": "c1a7de0ac9d94e4baceae031d05caae3",
                    "memory_mb": 512,
                    "project": "(used_now)"
                }
            },
            {
                "resource": {
                    "cpu": 0,
                    "disk_gb": 0,
                    "host": "c1a7de0ac9d94e4baceae031d05caae3",
                    "memory_mb": 0,
                    "project": "(used_max)"
                }
            }
        ]
    }
    

