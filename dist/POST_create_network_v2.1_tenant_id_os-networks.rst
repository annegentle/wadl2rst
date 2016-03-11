=============================================================================
Create Network -  OpenStack Compute API v2.1
=============================================================================

Create Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_network_v2.1_tenant_id_os-networks.rst#request>`__
`Response <POST_create_network_v2.1_tenant_id_os-networks.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-networks

Creates a network.

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








**Example Create Network: JSON request**


.. code::

    {"network": {"label": "new net 111","cidr": "10.20.105.0/24","mtu": 9000,"dhcp_server": "10.20.105.2","enable_dhcp": false,"share_address": true,"allowed_start": "10.20.105.10","allowed_end": "10.20.105.200"}}


Response
^^^^^^^^^^^^^^^^^^





**Example Create Network: JSON request**


.. code::

    {"network": {"bridge": null,"bridge_interface": null,"broadcast": "10.20.105.255","cidr": "10.20.105.0/24","cidr_v6": null,"created_at": null,"deleted": null,"deleted_at": null,"dhcp_server": "10.20.105.2","dhcp_start": "10.20.105.2","dns1": null,"dns2": null,"enable_dhcp": false,"gateway": "10.20.105.1","gateway_v6": null,"host": null,"id": "d7a17c0c-457e-4ab4-a99c-4fa1762f5359","injected": null,"label": "new net 111","mtu": 9000,"multi_host": null,"netmask": "255.255.255.0","netmask_v6": null,"priority": null,"project_id": null,"rxtx_base": null,"share_address": true,"updated_at": null,"vlan": null,"vpn_private_address": null,"vpn_public_address": null,"vpn_public_port": null}}

