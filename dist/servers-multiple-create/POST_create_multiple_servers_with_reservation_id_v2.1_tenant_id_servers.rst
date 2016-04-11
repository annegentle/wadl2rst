
Create Multiple Servers With Reservation Id
===========================================

`Request <POST_create_multiple_servers_with_reservation_id_v2.1_tenant_id_servers.rst#request>`__
`Response <POST_create_multiple_servers_with_reservation_id_v2.1_tenant_id_servers.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers

Creates one or more servers with a reservation ID.

Set ``"return_reservation_id": "True"`` in the request body to request that a reservation ID be returned instead of the newly created instance information. With this parameter, the response shows only the reservation ID.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../createMultipleServersWithReservationId.yaml

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




**Example Create multiple servers with reservation ID**


.. literalinclude:: ../../../doc/api_samples/servers-multiple-create/multiple-create-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../createMultipleServersWithReservationId.yaml

	- reservation_id: reservation_id




**Example Create multiple servers with reservation ID**


.. literalinclude:: ../../../doc/api_samples/servers-multiple-create/multiple-create-resp.json
   :language: javascript

