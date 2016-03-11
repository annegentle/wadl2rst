=============================================================================
Update Port -  OpenStack Compute API v2.1
=============================================================================

Update Port
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_port_v2.0_ports_port_id_.rst#request>`__
`Response <PUT_update_port_v2.0_ports_port_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/ports/{port_id}

Updates a port.

You can update information for a port, such as its symbolic name and associated IPs. When you update IPs for a port, any previously associated IPs are removed, returned to the respective subnet allocation pools, and replaced by the IPs in the request body. Therefore, this operation replaces the ``fixed_ip`` attribute when you specify it in the request body. If the updated IP addresses are not valid or are already in use, the operation fails and the existing IP addresses are not removed from the port.

When you update security groups for a port and the operation succeeds, any associated security groups are removed and replaced by the security groups in the request body. Therefore, this operation replaces the ``security_groups`` attribute when you specify it in the request body. If the security groups are not valid, the operation fails and the existing security groups are not removed from the port.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{port_id}                 |csapi:UUID *(Required)*  |The UUID of the port.    |
+--------------------------+-------------------------+-------------------------+





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





**Example Update Port: JSON request**


.. code::

    {"port": {"name": "test-for-port-update","admin_state_up": true,"device_owner": "compute:nova","binding:host_id": "test_for_port_update_host"}}


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





**Example Update Port: JSON request**


.. code::

    {"port": {"status": "DOWN","binding:host_id": "test_for_port_update_host","allowed_address_pairs": [],"extra_dhcp_opts": [],"device_owner": "compute:nova","binding:profile": {},"fixed_ips": [{"subnet_id": "898dec4a-74df-4193-985f-c76721bcc746","ip_address": "20.20.0.4"}],"id": "43c831e0-19ce-4a76-9a49-57b57e69428b","security_groups": ["ce0179d6-8a94-4f7c-91c2-f3038e2acbd0"],"device_id": "","name": "test-for-port-update","admin_state_up": true,"network_id": "883fc383-5ea1-4c8b-8916-e1ddb0a9f365","tenant_id": "522eda8d23124b25bf03fe44f1986b74","binding:vif_details": {},"binding:vnic_type": "normal","binding:vif_type": "binding_failed","mac_address": "fa:16:3e:11:11:5e"}}

