
Create Server
=============

`Request <POST_create_server_v2.1_tenant_id_servers.rst#request>`__
`Response <POST_create_server_v2.1_tenant_id_servers.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers

Creates a server.

The progress of this operation depends on the location of the requested image, network I/O, host load, selected flavor, and other factors.

To check the progress of the request, make a ``GET /servers/{id}`` request. This call returns a progress attribute, which is a percentage value from 0 to 100.

The ``Location`` header returns the full URL to the newly created server and is available as a ``self`` and ``bookmark`` link in the server representation.

When you create a server, the response shows only the server ID, its links, and the admin password. You can get additional attributes through subsequent ``GET`` requests on the server.

Include the ``block-device-mapping-v2`` parameter in the create request body to boot a server from a volume.

Include the ``key_name`` parameter in the create request body to add a keypair to the server when you create it. To create a keypair, make a `create keypair <http://developer.openstack.org/api-ref-compute-v2.1.html#createKeypair>`__ request.

Preconditions

The user must have sufficient server quota to create the number of servers requested.

The connection to the Image service is valid.

Asynchronous postconditions

With correct permissions, you can see the server status as ``ACTIVE`` through API calls.

With correct access, you can see the created server in the compute node that OpenStack Compute manages.

Troubleshooting

If the server status remains ``BUILDING`` or shows another error status, the request failed. Ensure you meet the preconditions then investigate the compute node.

The server is not created in the compute node that OpenStack Compute manages.

The compute node needs enough free resource to match the resource of the server creation request.

Ensure that the scheduler selection filter can fulfill the request with the available compute nodes that match the selection criteria of the filter.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: createServer.yaml

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




**Example Create Server: JSON request**


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
    


Response
^^^^^^^^


.. rest_parameters:: createServer.yaml

	- server: server
	- adminPass: adminPass
	- id: id
	- links: links
	- OS-DCF:diskConfig: OS-DCF:diskConfig
	- security_groups: security_groups




**Example Create Server: JSON request**


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
    

