=============================================================================
List Virtual Interfaces -  OpenStack Compute API v2.1
=============================================================================

List Virtual Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_virtual_interfaces_v2.1_tenant_id_servers_server_id_os-virtual-interfaces.rst#request>`__
`Response <GET_list_virtual_interfaces_v2.1_tenant_id_servers_server_id_os-virtual-interfaces.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/servers/{server_id}/os-virtual-interfaces

Lists the virtual interfaces for an instance.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Change these permissions through the ``policy.json`` file.

The API v2 returns the network ID in the ``OS-EXT-VIF-NET:net_id`` response attribute.

The API v2.1 base version does not return the network ID.

The API v2.12 microversion returns the network ID in the ``net_id`` response attribute.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|virtual_interfaces        |xsd:string *(Required)*  |A ``virtual_interfaces`` |
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
    

