=============================================================================
Create Project Network -  OpenStack Compute API v2.1
=============================================================================

Create Project Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_project_network_v2.1_tenant_id_os-tenant-networks.rst#request>`__
`Response <POST_create_project_network_v2.1_tenant_id_os-tenant-networks.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-tenant-networks

Creates a project network.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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








**Example Create Project Network: JSON request**


.. code::

    {
        "network": {
            "label": "public",
            "cidr": "172.0.0.0/24",
            "vlan_start": 1,
            "num_networks": 1,
            "network_size": 255
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Project Network: JSON request**


.. code::

    {
        "network": {
            "cidr": "172.0.0.0/24",
            "id": "5bbcc3c4-1da2-4437-a48a-66f15b1b13f9",
            "label": "public"
        }
    }
    

