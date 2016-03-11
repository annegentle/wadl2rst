=============================================================================
Add Interface To Bare Metal Node -  OpenStack Compute API v2.1
=============================================================================

Add Interface To Bare Metal Node
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_add_interface_to_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_action.rst#request>`__
`Response <POST_add_interface_to_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/action

Adds an interface to a bare metal node that is associated with a server.



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








**Example Add Interface To Bare Metal Node: JSON request**


.. code::

    {
        "add_interface": {
            "address": "aa:aa:aa:aa:aa:aa"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Add Interface To Bare Metal Node: JSON request**


.. code::

    {
        "interface": {
            "address": "aa:aa:aa:aa:aa:aa",
            "datapath_id": null,
            "id": 1,
            "port_no": null
        }
    }
    

