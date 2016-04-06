
List Virtual Interfaces
=======================

`Request <GET_list_virtual_interfaces_v2.1_tenant_id_servers_server_id_os-virtual-interfaces.rst#request>`__
`Response <GET_list_virtual_interfaces_v2.1_tenant_id_servers_server_id_os-virtual-interfaces.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-virtual-interfaces

Lists the virtual interfaces for an instance.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Change these permissions through the ``policy.json`` file.

The API v2 returns the network ID in the ``OS-EXT-VIF-NET:net_id`` response attribute.

The API v2.1 base version does not return the network ID.

The API v2.12 microversion returns the network ID in the ``net_id`` response attribute.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id







Response
^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|virtual_interfaces        |xsd:list *(Required)*    |A ``virtual_interfaces`` |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the virtual  |
|                          |                         |interface.               |
+--------------------------+-------------------------+-------------------------+
|mac_address               |xsd:string *(Required)*  |The MAC address.         |
+--------------------------+-------------------------+-------------------------+





**Example List Virtual Interfaces: JSON request**


.. code::

    {
        "virtual_interfaces": [
            {
                "id": "cec8b9bb-5d22-4104-b3c8-4c35db3210a6",
                "mac_address": "fa:16:3e:3c:ce:6f"
            }
        ]
    }
    

