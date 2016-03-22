=============================================================================
Delete Interface From Bare Metal Node -  OpenStack Compute API v2.1
=============================================================================

Delete Interface From Bare Metal Node
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_delete_interface_from_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_action.rst#request>`__
`Response <POST_delete_interface_from_bare_metal_node_v2.1_tenant_id_servers_server_id_os-baremetal-nodes_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/os-baremetal-nodes/action

Deletes an interface from a bare metal node that is associated with a server.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
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








**Example Delete Interface From Bare Metal Node: JSON request**


.. code::

    {
        "remove_interface": {
            "address": "aa:aa:aa:aa:aa:aa"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^




