=============================================================================
Show Server Group Details -  OpenStack Compute API v2.1
=============================================================================

Show Server Group Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_server_group_details_v2.1_tenant_id_os-server-groups_server_group_id_.rst#request>`__
`Response <GET_show_server_group_details_v2.1_tenant_id_os-server-groups_server_group_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-server-groups/{server_group_id}

Shows details for a server group.



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
|{server_group_id}         |csapi:UUID               |The UUID of the server   |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group            |xsd:string *(Required)*  |Security group object.   |
+--------------------------+-------------------------+-------------------------+





**Example Show Server Group Details: JSON request**


.. code::

    {
        "server_group": {
            "id": "5bbcc3c4-1da2-4437-a48a-66f15b1b13f9",
            "name": "test",
            "policies": [
                "anti-affinity"
            ],
            "members": [],
            "metadata": {}
        }
    }
    

