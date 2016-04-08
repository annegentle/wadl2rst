
Update Server
=============

`Request <PUT_update_server_v2.1_tenant_id_servers_server_id_.rst#request>`__
`Response <PUT_update_server_v2.1_tenant_id_servers_server_id_.rst#response>`__

.. rest_method:: PUT /v2.1/{tenant_id}/servers/{server_id}

Updates the editable attributes of a server.

Preconditions

The server must exist.

You can edit the ``accessIPv4``, ``accessIPv6``, ``diskConfig`` and ``name`` attributes.



Normal response codes: 200,,503,400,401,403,405,404,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: updateServer.yaml

	- security_groups: security_groups
	- user_data: user_data
	- os-availability-zone:availability_zone: os-availability-zone:availability_zone
	- server: server
	- imageRef: imageRef
	- flavorRef: flavorRef
	- networks: networks
	- uuid: uuid
	- port: port
	- fixed_ip: fixed_ip
	- name: name
	- metadata: metadata
	- personality: personality
	- block_device_mapping_v2: block_device_mapping_v2
	- device_name: device_name
	- source_type: source_type
	- destination_type: destination_type
	- delete_on_termination: delete_on_termination
	- guest_format: guest_format
	- boot_index: boot_index
	- config_drive: config_drive
	- key_name: key_name
	- os:scheduler_hints: os:scheduler_hints
	- OS-DCF:diskConfig: OS-DCF:diskConfig




**Example Update server name: JSON request**


.. code::

    {
        "server": {
            "name": "new-server-test",
            "imageRef": "http://glance.openstack.example.com/images/70a599e0-31e7-49b7-b260-868f441e862b",
            "flavorRef": "http://openstack.example.com/flavors/1",
            "metadata": {
                "My Server Name": "Apache1"
            }
        }
    }
    


**Example Update server IP addresses: JSON request**


.. code::

    {
        "server": {
            "accessIPv4": "192.0.2.0",
            "accessIPv6": "2002:0:0:0:0:0:c000:20e"
        }
    }
    


**Example Update server OS-DCF:diskConfig parameter: JSON request**


.. code::

    {
        "server": {
            "OS-DCF:diskConfig": "AUTO"
        }
    }
    


Response
^^^^^^^^


.. rest_parameters:: updateServer.yaml

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




**Example Update server name: JSON response**


.. code::

    {
        "server": {
            "id": "52415800-8b69-11e0-9b19-734f565bc83b",
            "tenant_id": "1234",
            "user_id": "5678",
            "name": "new-server-test",
            "created": "2010-11-11T12:00:00Z",
            "updated": "2010-11-12T12:44:44Z",
            "hostId": "e4d909c290d0fb1ca068ffaddf22cbd0",
            "accessIPv4": "192.0.2.0",
            "accessIPv6": "2002:0:0:0:0:0:c000:20e",
            "progress": 0,
            "status": "ACTIVE",
            "image": {
                "id": "52415800-8b69-11e0-9b19-734f6f006e54",
                "name": "CentOS 5.2",
                "links": [
                    {
                        "rel": "self",
                        "href": "http://servers.api.openstack.org/v2/1234/images/52415800-8b69-11e0-9b19-734f6f006e54"
                    },
                    {
                        "rel": "bookmark",
                        "href": "http://servers.api.openstack.org/1234/images/52415800-8b69-11e0-9b19-734f6f006e54"
                    }
                ]
            },
            "flavor": {
                "id": "52415800-8b69-11e0-9b19-734f1195ff37",
                "name": "256 MB Server",
                "links": [
                    {
                        "rel": "self",
                        "href": "http://servers.api.openstack.org/v2/1234/flavors/52415800-8b69-11e0-9b19-734f1195ff37"
                    },
                    {
                        "rel": "bookmark",
                        "href": "http://servers.api.openstack.org/1234/flavors/52415800-8b69-11e0-9b19-734f1195ff37"
                    }
                ]
            },
            "metadata": {
                "My Server Name": "Apache1"
            },
            "addresses": {
                "public": [
                    {
                        "version": 4,
                        "addr": "192.0.2.0"
                    },
                    {
                        "version": 6,
                        "addr": "2002:0:0:0:0:0:c000:20e"
                    }
                ],
                "private": [
                    {
                        "version": 4,
                        "addr": "198.51.100.0"
                    },
                    {
                        "version": 6,
                        "addr": "2002:0:0:0:0:0:c633:640e"
                    }
                ]
            },
            "links": [
                {
                    "rel": "self",
                    "href": "http://servers.api.openstack.org/v2/1234/servers/52415800-8b69-11e0-9b19-734fcece0043"
                },
                {
                    "rel": "bookmark",
                    "href": "http://servers.api.openstack.org/1234/servers/52415800-8b69-11e0-9b19-734fcece0043"
                }
            ]
        }
    }
    

