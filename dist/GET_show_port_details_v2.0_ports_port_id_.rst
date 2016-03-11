=============================================================================
Show Port Details -  OpenStack Compute API v2.1
=============================================================================

Show Port Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_port_details_v2.0_ports_port_id_.rst#request>`__
`Response <GET_show_port_details_v2.0_ports_port_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.0/ports/{port_id}

Shows details for a port.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{port_id}                 |csapi:UUID *(Required)*  |The UUID of the port.    |
+--------------------------+-------------------------+-------------------------+








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





**Example Show Port Details: JSON request**


.. code::

    {"port": {"status": "ACTIVE","name": "","allowed_address_pairs": [],"admin_state_up": true,"network_id": "a87cc70a-3e15-4acf-8205-9b711a3531b7","tenant_id": "7e02058126cc4950b75f9970368ba177","extra_dhcp_opts": [],"device_owner": "network:router_interface","mac_address": "fa:16:3e:23:fd:d7","fixed_ips": [{"subnet_id": "a0304c3a-4f08-4c43-88af-d796509c97d2","ip_address": "10.0.0.1"}],"id": "46d4bfb9-b26e-41f3-bd2e-e6dcc1ccedb2","security_groups": [],"device_id": "5e3898d7-11be-483e-9732-b2f5eccd2b2e"}}

