
Show Server Details
===================

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


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showServerDetails.yaml

	- tenant_id: tenant_id
	- server_id: server_id








Response
^^^^^^^^


.. rest_parameters:: ../showServerDetails.yaml

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


.. literalinclude:: ../../../doc/api_samples/servers/server-show-resp.json
   :language: javascript


