=============================================================================
List Ports -  OpenStack Compute API v2.1
=============================================================================

List Ports
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_ports_v2.0_ports.rst#request>`__
`Response <GET_list_ports_v2.0_ports.rst#response>`__

.. code-block:: javascript

    GET /v2.0/ports

Lists ports to which the tenant has access.

Default policy settings return only those ports that are owned by the tenant who submits the request, unless the request is submitted by a user with administrative rights. Users can control which attributes are returned by using the fields query parameter. You can use query parameters to filter the response.For information, see `Filtering and ColumnSelection <https://wiki.openstack.org/wiki/Neutron/APIv2-specification#Filtering_and_Column_Selection>`__.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^




This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|status                    |xsd:string *(Required)*  |The port status. Value   |
|                          |                         |is ``ACTIVE`` or         |
|                          |                         |``DOWN``.                |
+--------------------------+-------------------------+-------------------------+
|display_name              |xsd:string *(Required)*  |The port name.           |
+--------------------------+-------------------------+-------------------------+
|admin_state               |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the router, which is  |
|                          |                         |up ( ``true`` ) or down  |
|                          |                         |( ``false`` ).           |
+--------------------------+-------------------------+-------------------------+
|network_id                |csapi:UUID *(Required)*  |The UUID of the attached |
|                          |                         |network.                 |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |who owns the network.    |
|                          |                         |Only administrative      |
|                          |                         |users can specify a      |
|                          |                         |tenant UUID other than   |
|                          |                         |their own. You cannot    |
|                          |                         |change this value        |
|                          |                         |through authorization    |
|                          |                         |policies.                |
+--------------------------+-------------------------+-------------------------+
|device_owner              |xsd:string *(Required)*  |The UUID of the entity   |
|                          |                         |that uses this port. For |
|                          |                         |example, a DHCP agent.   |
+--------------------------+-------------------------+-------------------------+
|mac_address               |xsd:string *(Required)*  |The MAC address of the   |
|                          |                         |port.                    |
+--------------------------+-------------------------+-------------------------+
|port_id                   |csapi:UUID *(Required)*  |The UUID of the port.    |
+--------------------------+-------------------------+-------------------------+
|security_groups           |xsd:list *(Required)*    |The UUIDs of any         |
|                          |                         |attached security groups.|
+--------------------------+-------------------------+-------------------------+
|device_id                 |csapi:UUID *(Required)*  |The UUID of the device   |
|                          |                         |that uses this port. For |
|                          |                         |example, a virtual       |
|                          |                         |server.                  |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|ports                     |xsd:list *(Required)*    |A list of ``port``       |
|                          |                         |objects.                 |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The port status. Value   |
|                          |                         |is ``ACTIVE`` or         |
|                          |                         |``DOWN``.                |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The port name.           |
+--------------------------+-------------------------+-------------------------+
|allowed_address_pairs     |xsd:list *(Required)*    |A set of zero or more    |
|                          |                         |allowed address pairs.   |
|                          |                         |An address pair consists |
|                          |                         |of an IP address and MAC |
|                          |                         |address.                 |
+--------------------------+-------------------------+-------------------------+
|ip_address                |xsd:string *(Required)*  |The IP address.          |
+--------------------------+-------------------------+-------------------------+
|mac_address               |xsd:string *(Required)*  |The MAC address.         |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the port, which is up |
|                          |                         |( ``true`` ) or down (   |
|                          |                         |``false`` ).             |
+--------------------------+-------------------------+-------------------------+
|network_id                |csapi:UUID *(Required)*  |The UUID of the attached |
|                          |                         |network.                 |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |who owns the network.    |
|                          |                         |Only administrative      |
|                          |                         |users can specify a      |
|                          |                         |tenant UUID other than   |
|                          |                         |their own.               |
+--------------------------+-------------------------+-------------------------+
|extra_dhcp_opts           |xsd:list *(Required)*    |A set of zero or more    |
|                          |                         |extra DHCP option pairs. |
|                          |                         |An option pair consists  |
|                          |                         |of an option value and   |
|                          |                         |name.                    |
+--------------------------+-------------------------+-------------------------+
|opt_value                 |xsd:string *(Required)*  |The extra DHCP option    |
|                          |                         |value.                   |
+--------------------------+-------------------------+-------------------------+
|opt_name                  |xsd:string *(Required)*  |The extra DHCP option    |
|                          |                         |name.                    |
+--------------------------+-------------------------+-------------------------+
|device_owner              |xsd:string *(Required)*  |The UUID of the entity   |
|                          |                         |that uses this port. For |
|                          |                         |example, a DHCP agent.   |
+--------------------------+-------------------------+-------------------------+
|fixed_ips                 |xsd:list *(Required)*    |The IP addresses for the |
|                          |                         |port. Includes the IP    |
|                          |                         |address and UUID of the  |
|                          |                         |subnet.                  |
+--------------------------+-------------------------+-------------------------+
|subnet_id                 |csapi:UUID *(Required)*  |The UUID of the subnet   |
|                          |                         |to which the port is     |
|                          |                         |attached.                |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the port.    |
+--------------------------+-------------------------+-------------------------+
|security_groups           |xsd:list *(Required)*    |The UUIDs of any         |
|                          |                         |attached security groups.|
+--------------------------+-------------------------+-------------------------+
|device_id                 |csapi:UUID *(Required)*  |The UUID of the device   |
|                          |                         |that uses this port. For |
|                          |                         |example, a virtual       |
|                          |                         |server.                  |
+--------------------------+-------------------------+-------------------------+
|port_security_enabled     |xsd:boolean *(Required)* |The port security        |
|                          |                         |status. The status is    |
|                          |                         |enabled ( ``true`` ) or  |
|                          |                         |disabled ( ``false`` ).  |
+--------------------------+-------------------------+-------------------------+





**Example List Ports: JSON request**


.. code::

    {"ports": [{"status": "ACTIVE","name": "","allowed_address_pairs": [],"admin_state_up": true,"network_id": "70c1db1f-b701-45bd-96e0-a313ee3430b3","tenant_id": "","extra_dhcp_opts": [],"device_owner": "network:router_gateway","mac_address": "fa:16:3e:58:42:ed","fixed_ips": [{"subnet_id": "008ba151-0b8c-4a67-98b5-0d2b87666062","ip_address": "172.24.4.2"}],"id": "d80b1a3b-4fc1-49f3-952e-1e2ab7081d8b","security_groups": [],"device_id": "9ae135f4-b6e0-4dad-9e91-3c223e385824"},{"status": "ACTIVE","name": "","allowed_address_pairs": [],"admin_state_up": true,"network_id": "f27aa545-cbdd-4907-b0c6-c9e8b039dcc2","tenant_id": "d397de8a63f341818f198abb0966f6f3","extra_dhcp_opts": [],"device_owner": "network:router_interface","mac_address": "fa:16:3e:bb:3c:e4","fixed_ips": [{"subnet_id": "288bf4a1-51ba-43b6-9d0a-520e9005db17","ip_address": "10.0.0.1"}],"id": "f71a6703-d6de-4be1-a91a-a570ede1d159","security_groups": [],"device_id": "9ae135f4-b6e0-4dad-9e91-3c223e385824"}]}

