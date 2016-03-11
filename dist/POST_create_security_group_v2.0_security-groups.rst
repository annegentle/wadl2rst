=============================================================================
Create Security Group -  OpenStack Compute API v2.1
=============================================================================

Create Security Group
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_security_group_v2.0_security-groups.rst#request>`__
`Response <POST_create_security_group_v2.0_security-groups.rst#response>`__

.. code-block:: javascript

    POST /v2.0/security-groups

Creates an OpenStack Networking security group.

This operation creates a security group with default security group rules for the IPv4 and IPv6 ether types.



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


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group            |xsd:dict *(Required)*    |A ``security_group``     |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |A symbolic name for the  |
|                          |                         |security group. Does not |
|                          |                         |have to be unique.       |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The security group       |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |who owns the security    |
|                          |                         |group. Only              |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+





**Example Create Security Group: JSON request**


.. code::

    {"security_group": {"name": "new-webservers","description": "security group for webservers"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group            |xsd:dict *(Required)*    |A ``security_group``     |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The security group       |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID for the         |
|                          |                         |security group.          |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The security group name. |
+--------------------------+-------------------------+-------------------------+
|security_group_rules      |xsd:list *(Required)*    |A list of                |
|                          |                         |``security_group_rule``  |
|                          |                         |objects.                 |
+--------------------------+-------------------------+-------------------------+
|direction                 |xsd:string *(Required)*  |Ingress or egress: the   |
|                          |                         |direction in which the   |
|                          |                         |security group rule is   |
|                          |                         |applied. For a compute   |
|                          |                         |instance, an ingress     |
|                          |                         |security group rule is   |
|                          |                         |applied to incoming      |
|                          |                         |(ingress) traffic for    |
|                          |                         |that instance. An egress |
|                          |                         |rule is applied to       |
|                          |                         |traffic leaving the      |
|                          |                         |instance.                |
+--------------------------+-------------------------+-------------------------+
|ethertype                 |xsd:string *(Required)*  |Must be IPv4 or IPv6,    |
|                          |                         |and addresses            |
|                          |                         |represented in CIDR must |
|                          |                         |match the ingress or     |
|                          |                         |egress rules.            |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the security |
|                          |                         |group rule.              |
+--------------------------+-------------------------+-------------------------+
|port_range_max            |xsd:int *(Required)*     |The maximum port number  |
|                          |                         |in the range that is     |
|                          |                         |matched by the security  |
|                          |                         |group rule. The          |
|                          |                         |``port_range_min``       |
|                          |                         |attribute constrains the |
|                          |                         |``port_range_max``       |
|                          |                         |attribute. If the        |
|                          |                         |protocol is ICMP, this   |
|                          |                         |value must be an ICMP    |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+
|port_range_min            |xsd:int *(Required)*     |The minimum port number  |
|                          |                         |in the range that is     |
|                          |                         |matched by the security  |
|                          |                         |group rule. If the       |
|                          |                         |protocol is TCP or UDP,  |
|                          |                         |this value must be less  |
|                          |                         |than or equal to the     |
|                          |                         |``port_range_max``       |
|                          |                         |attribute value. If the  |
|                          |                         |protocol is ICMP, this   |
|                          |                         |value must be an ICMP    |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+
|protocol                  |xsd:string *(Required)*  |The protocol that is     |
|                          |                         |matched by the security  |
|                          |                         |group rule. Value is     |
|                          |                         |``null``, ``icmp``,      |
|                          |                         |``icmpv6``, ``tcp``, or  |
|                          |                         |``udp``.                 |
+--------------------------+-------------------------+-------------------------+
|remote_group_id           |csapi:UUID *(Required)*  |The remote group UUID to |
|                          |                         |associate with this      |
|                          |                         |security group rule. You |
|                          |                         |can specify either the   |
|                          |                         |``remote_group_id`` or   |
|                          |                         |``remote_ip_prefix``     |
|                          |                         |attribute in the request |
|                          |                         |body.                    |
+--------------------------+-------------------------+-------------------------+
|remote_ip_prefix          |xsd:string *(Required)*  |The remote IP prefix to  |
|                          |                         |associate with this      |
|                          |                         |security group rule. You |
|                          |                         |can specify either the   |
|                          |                         |``remote_group_id`` or   |
|                          |                         |``remote_ip_prefix``     |
|                          |                         |attribute in the request |
|                          |                         |body. This attribute     |
|                          |                         |value matches the IP     |
|                          |                         |prefix as the source IP  |
|                          |                         |address of the IP packet.|
+--------------------------+-------------------------+-------------------------+
|security_group_id         |csapi:UUID *(Required)*  |The UUID of the security |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |who owns the security    |
|                          |                         |group rule. Only         |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+





**Example Create Security Group: JSON request**


.. code::

    {"security_group": {"description": "security group for webservers","id": "2076db17-a522-4506-91de-c6dd8e837028","name": "new-webservers","security_group_rules": [{"direction": "egress","ethertype": "IPv4","id": "38ce2d8e-e8f1-48bd-83c2-d33cb9f50c3d","port_range_max": null,"port_range_min": null,"protocol": null,"remote_group_id": null,"remote_ip_prefix": null,"security_group_id": "2076db17-a522-4506-91de-c6dd8e837028","tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"},{"direction": "egress","ethertype": "IPv6","id": "565b9502-12de-4ffd-91e9-68885cff6ae1","port_range_max": null,"port_range_min": null,"protocol": null,"remote_group_id": null,"remote_ip_prefix": null,"security_group_id": "2076db17-a522-4506-91de-c6dd8e837028","tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"}],"tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"}}

