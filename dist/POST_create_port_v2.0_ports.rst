=============================================================================
Create Port -  OpenStack Compute API v2.1
=============================================================================

Create Port
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_port_v2.0_ports.rst#request>`__
`Response <POST_create_port_v2.0_ports.rst#response>`__

.. code-block:: javascript

    POST /v2.0/ports

Creates a port on a network.

To define the network in which to create the port, specify the ``network_id`` attribute in the request body.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|port                      |xsd:dict *(Required)*    |A ``port`` object.       |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |A symbolic name for the  |
|                          |                         |port.                    |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative       |
|                          |                         |status of the port,      |
|                          |                         |which is up ( ``true`` ) |
|                          |                         |or down ( ``false`` ).   |
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
|mac_address               |xsd:string *(Required)*  |The MAC address. If you  |
|                          |                         |specify an address that  |
|                          |                         |is not valid, a ``Bad    |
|                          |                         |Request (400)`` status   |
|                          |                         |code is returned. If you |
|                          |                         |do not specify a MAC     |
|                          |                         |address, OpenStack       |
|                          |                         |Networking tries to      |
|                          |                         |allocate one. If a       |
|                          |                         |failure occurs, a        |
|                          |                         |``Service Unavailable    |
|                          |                         |(503)`` response code is |
|                          |                         |returned.                |
+--------------------------+-------------------------+-------------------------+
|fixed_ips                 |xsd:list *(Required)*    |If you specify only a    |
|                          |                         |subnet UUID, OpenStack   |
|                          |                         |Networking allocates an  |
|                          |                         |available IP from that   |
|                          |                         |subnet to the port. If   |
|                          |                         |you specify both a       |
|                          |                         |subnet UUID and an IP    |
|                          |                         |address, OpenStack       |
|                          |                         |Networking tries to      |
|                          |                         |allocate the address to  |
|                          |                         |the port.                |
+--------------------------+-------------------------+-------------------------+
|subnet_id                 |csapi:UUID *(Required)*  |If you specify only a    |
|                          |                         |subnet UUID, OpenStack   |
|                          |                         |Networking allocates an  |
|                          |                         |available IP from that   |
|                          |                         |subnet to the port. If   |
|                          |                         |you specify both a       |
|                          |                         |subnet UUID and an IP    |
|                          |                         |address, OpenStack       |
|                          |                         |Networking tries to      |
|                          |                         |allocate the address to  |
|                          |                         |the port.                |
+--------------------------+-------------------------+-------------------------+
|ip_address                |xsd:string *(Required)*  |If you specify both a    |
|                          |                         |subnet UUID and an IP    |
|                          |                         |address, OpenStack       |
|                          |                         |Networking tries to      |
|                          |                         |allocate the address to  |
|                          |                         |the port.                |
+--------------------------+-------------------------+-------------------------+
|security_groups           |xsd:list *(Required)*    |One or more security     |
|                          |                         |group UUIDs.             |
+--------------------------+-------------------------+-------------------------+
|network_id                |csapi:UUID *(Required)*  |The UUID of the network. |
+--------------------------+-------------------------+-------------------------+
|allowed_address_pairs     |xsd:list *(Required)*    |A set of zero or more    |
|                          |                         |allowed address pairs.   |
|                          |                         |An address pair contains |
|                          |                         |an IP address and MAC    |
|                          |                         |address.                 |
+--------------------------+-------------------------+-------------------------+
|ip_address                |xsd:string *(Required)*  |The IP address of an     |
|                          |                         |allowed address pair.    |
+--------------------------+-------------------------+-------------------------+
|mac_address               |xsd:string *(Required)*  |The MAC address of an    |
|                          |                         |allowed address pair.    |
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
|device_id                 |csapi:UUID *(Required)*  |The UUID of the device   |
|                          |                         |that uses this port. For |
|                          |                         |example, a virtual       |
|                          |                         |server.                  |
+--------------------------+-------------------------+-------------------------+





**Example Create Port: JSON request**


.. code::

    {"port": {"network_id": "a87cc70a-3e15-4acf-8205-9b711a3531b7","name": "private-port","admin_state_up": true}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|port                      |xsd:dict *(Required)*    |A ``port`` object.       |
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





**Example Create Port: JSON request**


.. code::

    {"port": {"status": "DOWN","name": "private-port","allowed_address_pairs": [],"admin_state_up": true,"network_id": "a87cc70a-3e15-4acf-8205-9b711a3531b7","tenant_id": "d6700c0c9ffa4f1cb322cd4a1f3906fa","device_owner": "","mac_address": "fa:16:3e:c9:cb:f0","fixed_ips": [{"subnet_id": "a0304c3a-4f08-4c43-88af-d796509c97d2","ip_address": "10.0.0.2"}],"id": "65c0ee9f-d634-4522-8954-51021b570b0d","security_groups": ["f0ac4394-7e4a-4409-9701-ba8be283dbc3"],"device_id": ""}}

