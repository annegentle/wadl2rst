=============================================================================
Create Vpn Endpoint Group -  OpenStack Compute API v2.1
=============================================================================

Create Vpn Endpoint Group
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_vpn_endpoint_group_v2.0_vpn_endpoint-groups.rst#request>`__
`Response <POST_create_vpn_endpoint_group_v2.0_vpn_endpoint-groups.rst#response>`__

.. code-block:: javascript

    POST /v2.0/vpn/endpoint-groups

Creates a VPN endpoint group.

The endpoint group contains one or more endpoints of a specific type that you can use to create a VPN connections.



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
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the VPN endpoint group.  |
|                          |                         |Does not have to be      |
|                          |                         |unique.                  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the VPN  |
|                          |                         |endpoint group.          |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |Owner of the VPN         |
|                          |                         |endpoint group. Only     |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |The type of the          |
|                          |                         |endpoints in the group.  |
|                          |                         |A valid value is         |
|                          |                         |``subnet``, ``cidr``,    |
|                          |                         |``network``, ``router``, |
|                          |                         |or ``vlan``.             |
+--------------------------+-------------------------+-------------------------+
|endpoints                 |xsd:list *(Required)*    |List of endpoints of the |
|                          |                         |same type, for the       |
|                          |                         |endpoint group. The      |
|                          |                         |values will depend on    |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+





**Example Create Vpn Endpoint Group: JSON request**


.. code::

    {"endpoint_group": {"endpoints": ["10.2.0.0/24","10.3.0.0/24"],"type": "cidr","name": "peers"}}


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





**Example Create Vpn Endpoint Group: JSON request**


.. code::

    {"endpoint_group": {"description": "","tenant_id": "4ad57e7ce0b24fca8f12b9834d91079d","endpoints": ["10.2.0.0/24","10.3.0.0/24"],"type": "cidr","id": "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a","name": "peers"}}

