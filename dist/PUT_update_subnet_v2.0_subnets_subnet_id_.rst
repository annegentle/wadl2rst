=============================================================================
Update Subnet -  OpenStack Compute API v2.1
=============================================================================

Update Subnet
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_subnet_v2.0_subnets_subnet_id_.rst#request>`__
`Response <PUT_update_subnet_v2.0_subnets_subnet_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/subnets/{subnet_id}

Updates a subnet.

Some attributes, such as IP version (ip_version), and CIDR (cidr) cannot be updated. Attempting to update these attributes results in a ``400 Bad Request`` error.



This table shows the possible response codes for this operation:


+-----------------+----------------+-------------------------------------------+
|Response Code    |Name            |Description                                |
+=================+================+===========================================+
|200              |                |A ``subnet`` object. The subnet name. The  |
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


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{subnet_id}               |csapi:UUID               |The UUID of the subnet.  |
+--------------------------+-------------------------+-------------------------+





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
|allocation_pools |xsd:dict        |The start and end addresses for the        |
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





**Example Update Subnet: JSON request**


.. code::

    {"subnet": {"name": "my_subnet"}}


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





**Example Update Subnet: JSON request**


.. code::

    {"subnet": {"name": "my_subnet","enable_dhcp": true,"network_id": "db193ab3-96e3-4cb3-8fc5-05f4296d0324","tenant_id": "26a7980765d0414dbc1fc1f88cdb7e6e","dns_nameservers": [],"allocation_pools": [{"start": "10.0.0.2","end": "10.0.0.254"}],"host_routes": [],"ip_version": 4,"gateway_ip": "10.0.0.1","cidr": "10.0.0.0/24","id": "08eae331-0402-425a-923c-34f7cfe39c1b"}}

