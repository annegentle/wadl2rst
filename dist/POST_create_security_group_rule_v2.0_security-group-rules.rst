=============================================================================
Create Security Group Rule -  OpenStack Compute API v2.1
=============================================================================

Create Security Group Rule
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_security_group_rule_v2.0_security-group-rules.rst#request>`__
`Response <POST_create_security_group_rule_v2.0_security-group-rules.rst#response>`__

.. code-block:: javascript

    POST /v2.0/security-group-rules

Creates an OpenStack Networking security group rule.



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
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group_rule       |xsd:dict *(Required)*    |A                        |
|                          |                         |``security_group_rule``  |
|                          |                         |object.                  |
+--------------------------+-------------------------+-------------------------+
|direction                 |xsd:string *(Required)*  |Ingress or egress: The   |
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
|security_group_id         |csapi:UUID *(Required)*  |The security group UUID  |
|                          |                         |to associate with this   |
|                          |                         |security group rule.     |
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
|protocol                  |xsd:string *(Required)*  |The protocol that is     |
|                          |                         |matched by the security  |
|                          |                         |group rule. Valid values |
|                          |                         |are null, tcp, udp, and  |
|                          |                         |icmp.                    |
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
|remote_ip_prefix          |csapi:UUID *(Required)*  |The remote IP prefix to  |
|                          |                         |associate with this      |
|                          |                         |security group rule. You |
|                          |                         |can specify either the   |
|                          |                         |``remote_group_id`` or   |
|                          |                         |``remote_ip_prefix``     |
|                          |                         |attribute in the request |
|                          |                         |body. This attribute     |
|                          |                         |matches the IP prefix as |
|                          |                         |the source IP address of |
|                          |                         |the IP packet.           |
+--------------------------+-------------------------+-------------------------+





**Example Create Security Group Rule: JSON request**


.. code::

    {"security_group_rule": {"direction": "ingress","port_range_min": "80","ethertype": "IPv4","port_range_max": "80","protocol": "tcp","remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","security_group_id": "a7734e61-b545-452d-a3cd-0189cbd9747a"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_group_rule       |xsd:dict *(Required)*    |A                        |
|                          |                         |``security_group_rule``  |
|                          |                         |object.                  |
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





**Example Create Security Group Rule: JSON request**


.. code::

    {"security_group_rule": {"direction": "ingress","ethertype": "IPv4","id": "2bc0accf-312e-429a-956e-e4407625eb62","port_range_max": 80,"port_range_min": 80,"protocol": "tcp","remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","remote_ip_prefix": null,"security_group_id": "a7734e61-b545-452d-a3cd-0189cbd9747a","tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"}}

