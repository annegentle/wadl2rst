=============================================================================
Create Interface -  OpenStack Compute API v2.1
=============================================================================

Create Interface
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_interface_v2.1_tenant_id_servers_server_id_os-interface.rst#request>`__
`Response <POST_create_interface_v2.1_tenant_id_servers_server_id_os-interface.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/os-interface

Creates a port interface and uses it to attach a port to a server instance.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|415                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|interfaceAttachment       |xsd:string *(Required)*  |Specify the              |
|                          |                         |``interfaceAttachment``  |
|                          |                         |action in the request    |
|                          |                         |body.                    |
+--------------------------+-------------------------+-------------------------+
|port_id                   |csapi:UUID *(Required)*  |The ID of the port for   |
|                          |                         |which you want to create |
|                          |                         |an interface. The        |
|                          |                         |``net_id`` and           |
|                          |                         |``port_id`` parameters   |
|                          |                         |are mutually exclusive.  |
|                          |                         |If you do not specify    |
|                          |                         |the ``port_id``          |
|                          |                         |parameter, the OpenStack |
|                          |                         |Networking API v2.0      |
|                          |                         |allocates a port and     |
|                          |                         |creates an interface for |
|                          |                         |it on the network.       |
+--------------------------+-------------------------+-------------------------+
|net_id                    |csapi:UUID *(Required)*  |The ID of the network    |
|                          |                         |for which you want to    |
|                          |                         |create a port interface. |
|                          |                         |The ``net_id`` and       |
|                          |                         |``port_id`` parameters   |
|                          |                         |are mutually exclusive.  |
|                          |                         |If you do not specify    |
|                          |                         |the ``net_id``           |
|                          |                         |parameter, the OpenStack |
|                          |                         |Networking API v2.0 uses |
|                          |                         |the network information  |
|                          |                         |cache that is associated |
|                          |                         |with the instance.       |
+--------------------------+-------------------------+-------------------------+
|fixed_ips                 |xsd:list *(Required)*    |Fixed IP addresses with  |
|                          |                         |subnet IDs. If you       |
|                          |                         |request a specific fixed |
|                          |                         |IP address without a     |
|                          |                         |``net_id``, the request  |
|                          |                         |returns a ``Bad Request  |
|                          |                         |(400)`` response code.   |
+--------------------------+-------------------------+-------------------------+





**Example Create Interface: JSON request**


.. code::

    {
        "interfaceAttachment": {
            "port_id": "ce531f90-199f-48c0-816c-13e38010b442"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|fixed_ips                 |xsd:list *(Required)*    |Fixed IP addresses with  |
|                          |                         |subnet IDs.              |
+--------------------------+-------------------------+-------------------------+
|mac_addr                  |xsd:string *(Required)*  |The MAC address.         |
+--------------------------+-------------------------+-------------------------+
|net_id                    |csapi:UUID *(Required)*  |The network ID.          |
+--------------------------+-------------------------+-------------------------+
|port_id                   |csapi:UUID *(Required)*  |The port ID.             |
+--------------------------+-------------------------+-------------------------+
|port_state                |xsd:string *(Required)*  |The port state.          |
+--------------------------+-------------------------+-------------------------+





**Example Create Interface: JSON request**


.. code::

    {
        "interfaceAttachment": {
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
    }
    

