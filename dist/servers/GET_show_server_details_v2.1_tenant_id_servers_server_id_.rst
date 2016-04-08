
Show Server Details
===================

`Request <GET_show_server_details_v2.1_tenant_id_servers_server_id_.rst#request>`__
`Response <GET_show_server_details_v2.1_tenant_id_servers_server_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}

Shows details for a server.

Includes server details including configuration drive, extended status, and server usage information.

The extended status information appears in the ``OS-EXT-STS:vm_state``, ``OS-EXT-STS:power_state``, and ``OS-EXT-STS:task_state`` attributes.

The server usage information appears in the ``OS-SRV-USG:launched_at`` and ``OS-SRV-USG:terminated_at`` attributes.

To hide ``addresses`` information for instances in a certain state, set the ``osapi_hide_server_address_states`` configuration option. Set this option to a valid VM state in the ``nova.conf`` configuration file.

HostId is unique peraccount and is not globally unique.

Preconditions

The server must exist.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: showServerDetails.yaml

	- server: server
	- addresses: addresses
	- created: created
	- flavor: flavor
	- hostId: hostId
	- id: id
	- image: image
	- key_name: key_name
	- links: links
	- metadata: metadata
	- name: name
	- OS-DCF:diskConfig: OS-DCF:diskConfig
	- OS-EXT-AZ:availability_zone: OS-EXT-AZ:availability_zone
	- OS-EXT-SRV-ATTR:host: OS-EXT-SRV-ATTR:host
	- OS-EXT-SRV-ATTR:hypervisor_hostname: OS-EXT-SRV-ATTR:hypervisor_hostname
	- OS-EXT-SRV-ATTR:instance_name: OS-EXT-SRV-ATTR:instance_name
	- OS-EXT-STS:power_state: OS-EXT-STS:power_state
	- OS-EXT-STS:task_state: OS-EXT-STS:task_state
	- OS-EXT-STS:vm_state: OS-EXT-STS:vm_state
	- os-extended-volumes:volumes_attached: os-extended-volumes:volumes_attached
	- OS-SRV-USG:launched_at: OS-SRV-USG:launched_at
	- OS-SRV-USG:terminated_at: OS-SRV-USG:terminated_at
	- progress: progress
	- security_groups: security_groups
	- description: description
	- id: id
	- name: name
	- rules: rules
	- status: status
	- host_status: host_status
	- tenant_id: tenant_id
	- updated: updated
	- user_id: user_id




**Example Show Server Details: JSON request**


.. code::

    {
        "server": {
            "addresses": {
                "private": [
                    {
                        "addr": "192.168.0.3",
                        "OS-EXT-IPS-MAC:mac_addr": "aa:bb:cc:dd:ee:ff",
                        "OS-EXT-IPS:type": "fixed",
                        "version": 4
                    }
                ]
            },
            "created": "2013-09-23T13:37:00Z",
            "flavor": {
                "id": "1",
                "links": [
                    {
                        "href": "http://openstack.example.com/openstack/flavors/1",
                        "rel": "bookmark"
                    }
                ]
            },
            "hostId": "9cc36101a27c2a69c1a18241f6228454d9d7f466bd90c62db8e8b856",
            "id": "f474386b-4fb6-4e1f-b1d5-d6bf4437f7d5",
            "image": {
                "id": "70a599e0-31e7-49b7-b260-868f441e862b",
                "links": [
                    {
                        "href": "http://openstack.example.com/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
                        "rel": "bookmark"
                    }
                ]
            },
            "key_name": null,
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/servers/f474386b-4fb6-4e1f-b1d5-d6bf4437f7d5",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/servers/f474386b-4fb6-4e1f-b1d5-d6bf4437f7d5",
                    "rel": "bookmark"
                }
            ],
            "metadata": {
                "My Server Name": "Apache1"
            },
            "name": "new-server-test",
            "accessIPv4": "192.0.2.0",
            "accessIPv6": "2002:0:0:0:0:0:c000:20e",
            "config_drive": "",
            "OS-DCF:diskConfig": "AUTO",
            "OS-EXT-AZ:availability_zone": "nova",
            "OS-EXT-SRV-ATTR:host": "b8b357f7100d4391828f2177c922ef93",
            "OS-EXT-SRV-ATTR:hypervisor_hostname": "fake-mini",
            "OS-EXT-SRV-ATTR:instance_name": "instance-00000001",
            "OS-EXT-STS:power_state": 1,
            "OS-EXT-STS:task_state": null,
            "OS-EXT-STS:vm_state": "active",
            "os-extended-volumes:volumes_attached": [],
            "OS-SRV-USG:launched_at": "2013-09-23T13:37:00.880302",
            "OS-SRV-USG:terminated_at": null,
            "progress": 0,
            "security_groups": [
                {
                    "name": "default"
                }
            ],
            "status": "ACTIVE",
            "host_status": "UP",
            "tenant_id": "openstack",
            "updated": "2013-10-31T07:31:30Z",
            "user_id": "fake"
        }
    }
    

