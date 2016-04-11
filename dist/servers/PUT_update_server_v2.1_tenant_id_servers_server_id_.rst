
Update Server
=============

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


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../updateServer.yaml

	- tenant_id: tenant_id
	- server_id: server_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../updateServer.yaml

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


.. literalinclude:: ../../../doc/api_samples/servers/server-update-req.json
   :language: javascript



**Example Update server IP addresses: JSON request**


.. literalinclude:: ../../../doc/api_samples/servers/server-update-address-req.json
   :language: javascript



**Example Update server OS-DCF:diskConfig parameter: JSON request**


.. literalinclude:: ../../../doc/api_samples/servers/server-update-diskconfig-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../updateServer.yaml

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


.. literalinclude:: ../../../doc/api_samples/servers/server-update-resp.json
   :language: javascript


