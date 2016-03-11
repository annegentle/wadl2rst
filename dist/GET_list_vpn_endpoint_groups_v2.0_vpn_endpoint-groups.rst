=============================================================================
List Vpn Endpoint Groups -  OpenStack Compute API v2.1
=============================================================================

List Vpn Endpoint Groups
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_vpn_endpoint_groups_v2.0_vpn_endpoint-groups.rst#request>`__
`Response <GET_list_vpn_endpoint_groups_v2.0_vpn_endpoint-groups.rst#response>`__

.. code-block:: javascript

    GET /v2.0/vpn/endpoint-groups

Lists VPN endpoint groups.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |csapi:UUID *(Required)*  |The UUID for the VPN     |
|                          |                         |endpoint group.          |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |Owner of the VPN         |
|                          |                         |endpoint group. Only     |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the VPN endpoint group.  |
|                          |                         |Does not have to be      |
|                          |                         |unique.                  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the VPN  |
|                          |                         |endpoint group.          |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |The type of the          |
|                          |                         |endpoints in the group.  |
|                          |                         |A valid value is         |
|                          |                         |``subnet``, ``cidr``,    |
|                          |                         |``network``, ``router``, |
|                          |                         |or ``vlan``.             |
+--------------------------+-------------------------+-------------------------+
|endpoints                 |xsd:list *(Required)*    |A list of endpoints of   |
|                          |                         |the same type for the    |
|                          |                         |endpoint group. Theses   |
|                          |                         |values depend on the     |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+





**Example List Vpn Endpoint Groups: JSON request**


.. code::

    {"endpoint_groups": [{"description": "","tenant_id": "4ad57e7ce0b24fca8f12b9834d91079d","endpoints": ["a3da778c-adfb-46db-88b3-d2ce53290a89"],"type": "subnet","id": "6bf34c7c-864c-4948-a6d4-db791669f9d4","name": "locals"},{"description": "","tenant_id": "4ad57e7ce0b24fca8f12b9834d91079d","endpoints": ["10.2.0.0/24","10.3.0.0/24"],"type": "cidr","id": "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a","name": "peers"}]}

