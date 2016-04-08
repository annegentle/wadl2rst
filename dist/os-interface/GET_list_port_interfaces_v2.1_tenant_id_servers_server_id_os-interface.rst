
List Port Interfaces
====================

`Request <GET_list_port_interfaces_v2.1_tenant_id_servers_server_id_os-interface.rst#request>`__
`Response <GET_list_port_interfaces_v2.1_tenant_id_servers_server_id_os-interface.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-interface

Lists port interfaces that are attached to a server.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: listPortInterfaces.yaml

	- interfaceAttachment: interfaceAttachment
	- port_state: port_state
	- fixed_ips: fixed_ips
	- mac_addr: mac_addr
	- net_id: net_id
	- port_id: port_id




**Example List Port Interfaces: JSON request**


.. code::

    {
        "interfaceAttachments": [
            {
                "fixed_ips": [
                    {
                        "ip_address": "192.168.1.3",
                        "subnet_id": "f8a6e8f8-c2ec-497c-9f23-da9616de54ef"
                    }
                ],
                "mac_addr": "fa:16:3e:4c:2c:30",
                "net_id": "3cb9bc59-5699-4588-a4b1-b87f96708bc6",
                "port_id": "ce531f90-199f-48c0-816c-13e38010b442",
                "port_state": "ACTIVE"
            }
        ]
    }
    

