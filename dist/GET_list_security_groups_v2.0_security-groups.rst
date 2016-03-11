=============================================================================
List Security Groups -  OpenStack Compute API v2.1
=============================================================================

List Security Groups
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_security_groups_v2.0_security-groups.rst#request>`__
`Response <GET_list_security_groups_v2.0_security-groups.rst#response>`__

.. code-block:: javascript

    GET /v2.0/security-groups

Lists OpenStack Networking security groups to which the tenant has access.

The list shows the UUID for and the rules that are associated with each security group.



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









**Example List Security Groups: JSON request**


.. code::

    GET /v2.0/security-groupsAccept: application/json


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|security_groups           |xsd:list *(Required)*    |A list of                |
|                          |                         |``security_group``       |
|                          |                         |objects.                 |
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





**Example List Security Groups: JSON request**


.. code::

    {"security_groups": [{"description": "default","id": "85cc3048-abc3-43cc-89b3-377341426ac5","name": "default","security_group_rules": [{"direction": "egress","ethertype": "IPv6","id": "3c0e45ff-adaf-4124-b083-bf390e5482ff","port_range_max": null,"port_range_min": null,"protocol": null,"remote_group_id": null,"remote_ip_prefix": null,"security_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"},{"direction": "egress","ethertype": "IPv4","id": "93aa42e5-80db-4581-9391-3a608bd0e448","port_range_max": null,"port_range_min": null,"protocol": null,"remote_group_id": null,"remote_ip_prefix": null,"security_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"},{"direction": "ingress","ethertype": "IPv6","id": "c0b09f00-1d49-4e64-a0a7-8a186d928138","port_range_max": null,"port_range_min": null,"protocol": null,"remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","remote_ip_prefix": null,"security_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"},{"direction": "ingress","ethertype": "IPv4","id": "f7d45c89-008e-4bab-88ad-d6811724c51c","port_range_max": null,"port_range_min": null,"protocol": null,"remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","remote_ip_prefix": null,"security_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5","tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"}],"tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"}]}

