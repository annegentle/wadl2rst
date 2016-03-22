=============================================================================
Add Bare Metal Node -  OpenStack Compute API v2.1
=============================================================================

Add Bare Metal Node
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_add_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes.rst#request>`__
`Response <POST_add_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes

Adds a bare metal node to a server.

Preconditions

You can add a bare metal node to a server with an ``ACTIVE``, ``PAUSED``, ``SHUTOFF``, ``VERIFY_RESIZE``, or ``SOFT_DELETED`` status.

You can add a bare metal node to a server with a status that is not locked.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|415                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
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
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+








**Example Add Bare Metal Node: JSON request**


.. code::

    {
        "node": {
            "service_host": "host",
            "cpus": 8,
            "memory_mb": 8192,
            "local_gb": 128,
            "pm_address": "10.1.2.3",
            "pm_user": "pm_user",
            "pm_password": "pm_pass",
            "terminal_port": 8000
        }
    }
    


**Example Add Bare Metal Node: JSON request**


.. code::

    {
        "node": {
            "service_host": "host",
            "cpus": 8,
            "memory_mb": 8192,
            "local_gb": 128,
            "pm_address": "10.1.2.3",
            "pm_user": "pm_user",
            "pm_password": "pm_pass",
            "prov_mac_address": "12:34:56:78:90:ab",
            "terminal_port": 8000
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Add Bare Metal Node: JSON request**


.. code::

    {
        "node": {
            "cpus": 8,
            "id": 1,
            "instance_uuid": null,
            "interfaces": [],
            "local_gb": 128,
            "memory_mb": 8192,
            "pm_address": "10.1.2.3",
            "pm_user": "pm_user",
            "pxe_config_path": null,
            "service_host": "host",
            "task_state": null,
            "terminal_port": 8000,
            "updated_at": null,
            "uuid": "73d35253-b6fb-4c83-b8eb-0229336e79b6"
        }
    }
    


**Example Add Bare Metal Node: JSON request**


.. code::

    {
        "node": {
            "cpus": 8,
            "id": 1,
            "instance_uuid": null,
            "interfaces": [
                {
                    "address": "12:34:56:78:90:ab",
                    "datapath_id": null,
                    "id": 1,
                    "port_no": null
                }
            ],
            "local_gb": 128,
            "memory_mb": 8192,
            "pm_address": "10.1.2.3",
            "pm_user": "pm_user",
            "pxe_config_path": null,
            "service_host": "host",
            "task_state": null,
            "terminal_port": 8000,
            "updated_at": null,
            "uuid": "0a130464-bccc-4e36-b9d3-9a8c98e636ae"
        }
    }
    

