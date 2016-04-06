
Show Network Details
====================

`Request <GET_show_network_details_v2.1_tenant_id_os-networks_network_id_.rst#request>`__
`Response <GET_show_network_details_v2.1_tenant_id_os-networks_network_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-networks/{network_id}

Shows details for a network.

Policy defaults enable all users to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- network_id: network_id







Response
^^^^^^^^





**Example Show Network Details: JSON request**


.. code::

    {
        "network": {
            "bridge": "br100",
            "bridge_interface": "eth0",
            "broadcast": "10.0.0.7",
            "cidr": "10.0.0.0/29",
            "cidr_v6": null,
            "created_at": "2011-08-15T06:19:19.387525",
            "deleted": false,
            "deleted_at": null,
            "dhcp_server": "10.0.0.1",
            "dhcp_start": "10.0.0.3",
            "dns1": null,
            "dns2": null,
            "enable_dhcp": true,
            "gateway": "10.0.0.1",
            "gateway_v6": null,
            "host": "nsokolov-desktop",
            "id": "20c8acc0-f747-4d71-a389-46d078ebf047",
            "injected": false,
            "label": "mynet_0",
            "mtu": null,
            "multi_host": false,
            "netmask": "255.255.255.248",
            "netmask_v6": null,
            "priority": null,
            "project_id": "1234",
            "rxtx_base": null,
            "share_address": false,
            "updated_at": "2011-08-16T09:26:13.048257",
            "vlan": 100,
            "vpn_private_address": "10.0.0.2",
            "vpn_public_address": "127.0.0.1",
            "vpn_public_port": 1000
        }
    }
    

