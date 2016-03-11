=============================================================================
List Subnets -  OpenStack Compute API v2.1
=============================================================================

List Subnets
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_subnets_v2.0_subnets.rst#request>`__
`Response <GET_list_subnets_v2.0_subnets.rst#response>`__

.. code-block:: javascript

    GET /v2.0/subnets

Lists subnets to which the tenant has access.

Default policy settings returns exclusively subnets owned by the tenant submitting the request, unless the request is submitted by a user with administrative rights. You can control which attributes are returned by using the fields query parameter. You can filter results by using query string parameters.



This table shows the possible response codes for this operation:


+-----------------+----------------+-------------------------------------------+
|Response Code    |Name            |Description                                |
+=================+================+===========================================+
|200              |                |A list of ``subnet`` objects. The subnet   |
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
|401              |                |                                           |
+-----------------+----------------+-------------------------------------------+


Request
^^^^^^^^^^^^^^^^^




This table shows the query parameters for the request:

+-------------------------+------------------------+---------------------------+
|Name                     |Type                    |Description                |
+=========================+========================+===========================+
|display_name             |xsd:string *(Required)* |Name of the network.       |
+-------------------------+------------------------+---------------------------+
|network_id               |csapi:uuid *(Required)* |The ID of the attached     |
|                         |                        |network.                   |
+-------------------------+------------------------+---------------------------+
|gateway_ip               |xsd:string *(Required)* |The gateway IP address.    |
+-------------------------+------------------------+---------------------------+
|ip_version               |xsd:int *(Required)*    |The IP version, which is 4 |
|                         |                        |or 6.                      |
+-------------------------+------------------------+---------------------------+
|cidr                     |xsd:string *(Required)* |The CIDR.                  |
+-------------------------+------------------------+---------------------------+
|id                       |csapi:uuid *(Required)* |The ID of the subnet.      |
+-------------------------+------------------------+---------------------------+
|enable_dhcp              |xsd:boolean *(Required)*|If true, DHCP is enabled   |
|                         |                        |and If false, DHCP is      |
|                         |                        |disabled.                  |
+-------------------------+------------------------+---------------------------+
|ipv6_ra_mode             |xsd:string *(Required)* |Choose from                |
|                         |                        |(constants.IPV6_SLAAC,     |
|                         |                        |constants.DHCPV6_STATEFUL, |
|                         |                        |constants.DH               |
|                         |                        |CPV6_STATELESS,            |
|                         |                        |name='ipv6_address_modes,  |
|                         |                        |null).                     |
+-------------------------+------------------------+---------------------------+
|ipv6_address_mode        |xsd:string *(Required)* |Choose from                |
|                         |                        |(constants.IPV6_SLAAC,     |
|                         |                        |constants.DHCPV6_STATEFUL, |
|                         |                        |constants.DH               |
|                         |                        |CPV6_STATELESS,            |
|                         |                        |name='ipv6_address_modes,  |
|                         |                        |null).                     |
+-------------------------+------------------------+---------------------------+




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
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





**Example List Subnets: JSON request**


.. code::

    {"subnets": [{"name": "private-subnet","enable_dhcp": true,"network_id": "db193ab3-96e3-4cb3-8fc5-05f4296d0324","tenant_id": "26a7980765d0414dbc1fc1f88cdb7e6e","dns_nameservers": [],"allocation_pools": [{"start": "10.0.0.2","end": "10.0.0.254"}],"host_routes": [],"ip_version": 4,"gateway_ip": "10.0.0.1","cidr": "10.0.0.0/24","id": "08eae331-0402-425a-923c-34f7cfe39c1b"},{"name": "my_subnet","enable_dhcp": true,"network_id": "d32019d3-bc6e-4319-9c1d-6722fc136a22","tenant_id": "4fd44f30292945e481c7b8a0c8908869","dns_nameservers": [],"allocation_pools": [{"start": "192.0.0.2","end": "192.255.255.254"}],"host_routes": [],"ip_version": 4,"gateway_ip": "192.0.0.1","cidr": "192.0.0.0/8","id": "54d6f61d-db07-451c-9ab3-b9609b6b6f0b"}]}

