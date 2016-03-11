=============================================================================
Bulk Create Subnet -  OpenStack Compute API v2.1
=============================================================================

Bulk Create Subnet
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_bulk_create_subnet_v2.0_subnets.rst#request>`__
`Response <POST_bulk_create_subnet_v2.0_subnets.rst#response>`__

.. code-block:: javascript

    POST /v2.0/subnets

Creates multiple subnets in a single request. Specify a list of subnets in the request body.

The bulk create operation is always atomic. Either all or no subnets in the request body are created.



This table shows the possible response codes for this operation:


+-----------------+----------------+-------------------------------------------+
|Response Code    |Name            |Description                                |
+=================+================+===========================================+
|201              |                |A list of ``subnet`` objects. The subnet   |
|                 |                |name. The UUID of the attached network.    |
|                 |                |The UUID of the tenant who owns the        |
|                 |                |network. Only administrative users can     |
|                 |                |specify a tenant UUID other than their     |
|                 |                |own. You cannot change this value through  |
|                 |                |authorization policies. The start and end  |
|                 |                |addresses for the allocation pools. The    |
|                 |                |start address for the allocation pools.    |
|                 |                |The end address for the allocation pools.  |
|                 |                |The gateway IP address. The IP version,    |
|                 |                |which is 4 or 6. The CIDR. The UUID of the |
|                 |                |subnet. Set to ``true`` if DHCP is enabled |
|                 |                |and ``false`` if DHCP is disabled. The DNS |
|                 |                |server. A list of host route dictionaries  |
|                 |                |for the subnet. For example:               |
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
|subnets          |xsd:list        |A list of ``subnet`` objects.              |
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





**Example Bulk Create Subnet: JSON request**


.. code::

    {"subnets": [{"cidr": "192.168.199.0/24","ip_version": 4,"network_id": "e6031bc2-901a-4c66-82da-f4c32ed89406"},{"cidr": "10.56.4.0/22","ip_version": 4,"network_id": "64239a54-dcc4-4b39-920b-b37c2144effa"}]}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+-----------------+----------------+-------------------------------------------+
|Name             |Type            |Description                                |
+=================+================+===========================================+
|subnets          |xsd:list        |A list of ``subnet`` objects.              |
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





**Example Bulk Create Subnet: JSON request**


.. code::

    {"subnets": [{"allocation_pools": [{"end": "192.168.199.254","start": "192.168.199.2"}],"cidr": "192.168.199.0/24","dns_nameservers": [],"enable_dhcp": true,"gateway_ip": "192.168.199.1","host_routes": [],"id": "0468a7a7-290d-4127-aedd-6c9449775a24","ip_version": 4,"name": "","network_id": "e6031bc2-901a-4c66-82da-f4c32ed89406","tenant_id": "d19231fc08ec4bc4829b668040d34512"},{"allocation_pools": [{"end": "10.56.7.254","start": "10.56.4.2"}],"cidr": "10.56.4.0/22","dns_nameservers": [],"enable_dhcp": true,"gateway_ip": "10.56.4.1","host_routes": [],"id": "b0e7435c-1512-45fb-aa9e-9a7c5932fb30","ip_version": 4,"name": "","network_id": "64239a54-dcc4-4b39-920b-b37c2144effa","tenant_id": "d19231fc08ec4bc4829b668040d34512"}]}

