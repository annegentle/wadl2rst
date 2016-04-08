
Create Multiple Servers
=======================

`Request <POST_create_multiple_servers_v2.1_tenant_id_servers.rst#request>`__
`Response <POST_create_multiple_servers_v2.1_tenant_id_servers.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers

Creates one or more servers.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: createMultipleServers.yaml

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
	- return_reservation_id: return_reservation_id




**Example Create multiple servers without reservation ID**


.. code::

    {
        "server": {
            "name": "new-server-test",
            "imageRef": "http://openstack.example.com/openstack/images/70a599e0-31e7-49b7-b260-868f441e862b",
            "flavorRef": "http://openstack.example.com/openstack/flavors/1",
            "metadata": {
                "My Server Name": "Apache1"
            },
            "min_count": "2",
            "max_count": "3"
        }
    }
    


Response
^^^^^^^^


.. rest_parameters:: createMultipleServers.yaml

	- server: server
	- adminPass: adminPass
	- id: id
	- links: links
	- OS-DCF:diskConfig: OS-DCF:diskConfig
	- security_groups: security_groups




**Example Create multiple servers without reservation ID**


.. code::

    {
        "server": {
            "OS-DCF:diskConfig": "AUTO",
            "adminPass": "zPnp2GseTqG4",
            "id": "8195065c-fea4-4d57-b93f-5c5c63fe90e8",
            "links": [
                {
                    "href": "http://openstack.example.com/v2/openstack/servers/8195065c-fea4-4d57-b93f-5c5c63fe90e8",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/openstack/servers/8195065c-fea4-4d57-b93f-5c5c63fe90e8",
                    "rel": "bookmark"
                }
            ],
            "security_groups": [
                {
                    "name": "default"
                }
            ]
        }
    }
    

