=============================================================================
Update Vpn Endpoint Group -  OpenStack Compute API v2.1
=============================================================================

Update Vpn Endpoint Group
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_vpn_endpoint_group_v2.0_vpn_endpoint-groups_endpoint_group_id_.rst#request>`__
`Response <PUT_update_vpn_endpoint_group_v2.0_vpn_endpoint-groups_endpoint_group_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/vpn/endpoint-groups/{endpoint_group_id}

Updates settings for a VPN endpoint group.



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
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{endpoint_group_id}       |csapi:UUID               |The UUID of the VPN      |
|                          |                         |endpoint group.          |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the VPN endpoint group.  |
|                          |                         |Does not have to be      |
|                          |                         |unique.                  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the VPN  |
|                          |                         |endpoint group.          |
+--------------------------+-------------------------+-------------------------+





**Example Update Vpn Endpoint Group: JSON request**


.. code::

    {"endpoint_group": {"description": "New description"}}


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





**Example Update Vpn Endpoint Group: JSON request**


.. code::

    {"endpoint_group": {"description": "New description","tenant_id": "4ad57e7ce0b24fca8f12b9834d91079d","endpoints": ["10.2.0.0/24","10.3.0.0/24"],"type": "cidr","id": "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a","name": "peers"}}

