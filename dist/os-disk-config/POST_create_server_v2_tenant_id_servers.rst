
Create Server
=============

`Request <POST_create_server_v2_tenant_id_servers.rst#request>`__
`Response <POST_create_server_v2_tenant_id_servers.rst#response>`__

.. rest_method:: POST /v2/{tenant_id}/servers

Creates a server.



Normal response codes: 202

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
	- os-disk-config:diskConfig: os-disk-config:diskConfig




**Example Create Server: JSON request**


.. code::

    


Response
^^^^^^^^


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




**Example Create Server: JSON request**


.. code::

    

