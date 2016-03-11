=============================================================================
Create Subnet -  OpenStack Compute API v2.1
=============================================================================

Create Subnet
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_subnet_v2.0_subnets.rst#request>`__
`Response <POST_create_subnet_v2.0_subnets.rst#response>`__

.. code-block:: javascript

    POST /v2.0/subnets

Creates a subnet on a network.

OpenStack Networking does not try to derive the correct IP version from the CIDR. If you do not specify the ``gateway_ip`` attribute, OpenStack Networking allocates an address from the CIDR for the gateway for the subnet.

To specify a subnet without a gateway, set the ``gateway_ip`` attribute to ``null`` in the request body. If you do not specify the ``allocation_pools`` attribute, OpenStack Networking automatically allocates pools for covering all IP addresses in the CIDR, excluding the address reserved for the subnet gateway. Otherwise, you can explicitly specify allocation pools as shown in the following example.

When you specify both the ``allocation_pools`` and ``gateway_ip`` attributes, you must ensure that the gateway IP does not overlap with the allocation pools; otherwise, the call returns the ``Conflict (409)`` response code.

A subnet can have one or more name servers and host routes. Hosts in this subnet use the name servers. Devices with IP addresses from this subnet, not including the local subnet route, use the host routes.

Specify the ``ipv6_ra_mode`` and ``ipv6_address_mode`` attributes to create subnets that support IPv6 configurations, such as stateless address autoconfiguration (SLAAC), DHCPv6 stateful, and DHCPv6 stateless configurations.



This table shows the possible response codes for this operation:


+-----------------+----------------+-------------------------------------------+
|Response Code    |Name            |Description                                |
+=================+================+===========================================+
|201              |                |A ``subnet`` object. The subnet name. The  |
|                 |                |UUID of the attached network. The UUID of  |
|                 |                |the tenant who owns the network. Only      |
|                 |                |administrative users can specify a tenant  |
|                 |                |UUID other than their own. You cannot      |
|                 |                |change this value through authorization    |
|                 |                |policies. The start and end addresses for  |
|                 |                |the allocation pools. The start address    |
|                 |                |for the allocation pools. The end address  |
|                 |                |for the allocation pools. The gateway IP   |
|                 |                |address. The IP version, which is 4 or 6.  |
|                 |                |The CIDR. The UUID of the subnet. Set to   |
|                 |                |``true`` if DHCP is enabled and ``false``  |
|                 |                |if DHCP is disabled. The DNS server. A     |
|                 |                |list of host route dictionaries for the    |
|                 |                |subnet. For example:                       |
|                 |                |"host_routes":[{"destination":"0.0.0.0/0", |
|                 |                |"nexthop":"123.456.78.9"},                 |
|                 |                |{"destination":"192.168.0.0/24",           |
|                 |                |"nexthop":"192.168.0.1"}]The destination   |
|                 |                |for static route. The next hop for the     |
|                 |                |destination. The IPv6 RA mode, which is    |
|                 |                |``dhcpv6-stateful``, ``dhcpv6-stateless``, |
|                 |                |or ``slaac``. The IPv6 address mode, which |
|                 |                |is ``dhcpv6-stateful``, ``dhcpv6-          |
|                 |                |stateless``, or ``slaac``.                 |
+-----------------+----------------+-------------------------------------------+
|400              |                |                                           |
+-----------------+----------------+-------------------------------------------+
|401              |                |                                           |
+-----------------+----------------+-------------------------------------------+
|403              |                |                                           |
+-----------------+----------------+-------------------------------------------+
|404              |                |                                           |
+-----------------+----------------+-------------------------------------------+
|409              |                |                                           |
+-----------------+----------------+-------------------------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+-----------------+----------------+-------------------------------------------+
|Name             |Type            |Description                                |
+=================+================+===========================================+
|subnet           |xsd:dict        |A ``subnet`` object.                       |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|name             |xsd:string      |The subnet name.                           |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|network_id       |csapi:UUID      |The UUID of the attached network.          |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|tenant_id        |csapi:UUID      |The UUID of the tenant who owns the        |
|                 |*(Required)*    |network. Only administrative users can     |
|                 |                |specify a tenant UUID other than their     |
|                 |                |own. You cannot change this value through  |
|                 |                |authorization policies.                    |
+-----------------+----------------+-------------------------------------------+
|allocation_pools |xsd:list        |The start and end addresses for the        |
|                 |*(Required)*    |allocation pools.                          |
+-----------------+----------------+-------------------------------------------+
|start            |xsd:string      |The start address for the allocation pools.|
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|end              |xsd:string      |The end address for the allocation pools.  |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|gateway_ip       |xsd:string      |The gateway IP address.                    |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|ip_version       |xsd:int         |The IP version, which is 4 or 6.           |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|cidr             |xsd:string      |The CIDR.                                  |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|enable_dhcp      |xsd:boolean     |Set to ``true`` if DHCP is enabled and     |
|                 |*(Required)*    |``false`` if DHCP is disabled.             |
+-----------------+----------------+-------------------------------------------+
|dns_nameservers  |xsd:list        |A list of DNS name servers for the subnet. |
|                 |*(Required)*    |Specify each name server as an IP address  |
|                 |                |and separate multiple entries with a       |
|                 |                |space. For example [8.8.8.7 8.8.8.8].      |
+-----------------+----------------+-------------------------------------------+
|host_routes      |xsd:list        |A list of host route dictionaries for the  |
|                 |*(Required)*    |subnet. For example:                       |
|                 |                |"host_routes":[{"destination":"0.0.0.0/0", |
|                 |                |"nexthop":"123.456.78.9"},                 |
|                 |                |{"destination":"192.168.0.0/24",           |
|                 |                |"nexthop":"192.168.0.1"}]                  |
+-----------------+----------------+-------------------------------------------+
|destination      |xsd:string      |The destination for static route.          |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|nexthop          |xsd:string      |The next hop for the destination.          |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|ipv6_ra_mode     |xsd:string      |A valid value is ``dhcpv6-stateful``,      |
|                 |*(Required)*    |``dhcpv6-stateless``, or ``slaac``.        |
+-----------------+----------------+-------------------------------------------+
|ipv6_address_mode|xsd:string      |A valid value is ``dhcpv6-stateful``,      |
|                 |*(Required)*    |``dhcpv6-stateless``, or ``slaac``.        |
+-----------------+----------------+-------------------------------------------+





**Example Create Subnet: JSON request**


.. code::

    {"subnet": {"network_id": "d32019d3-bc6e-4319-9c1d-6722fc136a22","ip_version": 4,"cidr": "10.0.0.1"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+-----------------+----------------+-------------------------------------------+
|Name             |Type            |Description                                |
+=================+================+===========================================+
|subnet           |xsd:dict        |A ``subnet`` object.                       |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|name             |xsd:string      |The subnet name.                           |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|network_id       |csapi:UUID      |The UUID of the attached network.          |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|tenant_id        |csapi:UUID      |The UUID of the tenant who owns the        |
|                 |*(Required)*    |network. Only administrative users can     |
|                 |                |specify a tenant UUID other than their     |
|                 |                |own. You cannot change this value through  |
|                 |                |authorization policies.                    |
+-----------------+----------------+-------------------------------------------+
|allocation_pools |xsd:list        |The start and end addresses for the        |
|                 |*(Required)*    |allocation pools.                          |
+-----------------+----------------+-------------------------------------------+
|start            |xsd:string      |The start address for the allocation pools.|
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|end              |xsd:string      |The end address for the allocation pools.  |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|gateway_ip       |xsd:string      |The gateway IP address.                    |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|ip_version       |xsd:int         |The IP version, which is 4 or 6.           |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|cidr             |xsd:string      |The CIDR.                                  |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|id               |csapi:UUID      |The UUID of the subnet.                    |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|enable_dhcp      |xsd:boolean     |Set to ``true`` if DHCP is enabled and     |
|                 |*(Required)*    |``false`` if DHCP is disabled.             |
+-----------------+----------------+-------------------------------------------+
|dns_nameservers  |xsd:list        |The DNS server.                            |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|host_routes      |xsd:list        |A list of host route dictionaries for the  |
|                 |*(Required)*    |subnet. For example:                       |
|                 |                |"host_routes":[{"destination":"0.0.0.0/0", |
|                 |                |"nexthop":"123.456.78.9"},                 |
|                 |                |{"destination":"192.168.0.0/24",           |
|                 |                |"nexthop":"192.168.0.1"}]                  |
+-----------------+----------------+-------------------------------------------+
|destination      |xsd:string      |The destination for static route.          |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|nexthop          |xsd:string      |The next hop for the destination.          |
|                 |*(Required)*    |                                           |
+-----------------+----------------+-------------------------------------------+
|ipv6_ra_mode     |xsd:string      |The IPv6 RA mode, which is ``dhcpv6-       |
|                 |*(Required)*    |stateful``, ``dhcpv6-stateless``, or       |
|                 |                |``slaac``.                                 |
+-----------------+----------------+-------------------------------------------+
|ipv6_address_mode|xsd:string      |The IPv6 address mode, which is ``dhcpv6-  |
|                 |*(Required)*    |stateful``, ``dhcpv6-stateless``, or       |
|                 |                |``slaac``.                                 |
+-----------------+----------------+-------------------------------------------+





**Example Create Subnet: JSON request**


.. code::

    {"subnet": {"name": "","enable_dhcp": true,"network_id": "d32019d3-bc6e-4319-9c1d-6722fc136a22","tenant_id": "4fd44f30292945e481c7b8a0c8908869","dns_nameservers": [],"allocation_pools": [{"start": "192.168.199.2","end": "192.168.199.254"}],"host_routes": [],"ip_version": 4,"gateway_ip": "192.168.199.1","cidr": "192.168.199.0/24","id": "3b80198d-4f7b-4f77-9ef5-774d54e17126"}}

