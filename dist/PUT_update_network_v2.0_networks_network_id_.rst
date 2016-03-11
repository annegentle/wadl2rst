=============================================================================
Update Network -  OpenStack Compute API v2.1
=============================================================================

Update Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_network_v2.0_networks_network_id_.rst#request>`__
`Response <PUT_update_network_v2.0_networks_network_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/networks/{network_id}

Updates a network.



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
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{network_id}              |csapi:UUID *(Required)*  |The UUID of the network. |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|network                   |xsd:dict *(Required)*    |A ``network`` object.    |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the network, which is |
|                          |                         |up ( ``true`` ) or down  |
|                          |                         |( ``false`` ).           |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The network name.        |
+--------------------------+-------------------------+-------------------------+
|shared                    |xsd:boolean *(Required)* |Admin-only. Indicates    |
|                          |                         |whether this network is  |
|                          |                         |shared across all        |
|                          |                         |tenants.                 |
+--------------------------+-------------------------+-------------------------+
|router:external           |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |network is externally    |
|                          |                         |accessible.              |
+--------------------------+-------------------------+-------------------------+
|port_security_enabled     |xsd:boolean *(Required)* |The port security        |
|                          |                         |status. A valid value is |
|                          |                         |enabled ( ``true`` ) or  |
|                          |                         |disabled ( ``false`` ).  |
+--------------------------+-------------------------+-------------------------+





**Example Update Network: JSON request**


.. code::

    {"network": {"name": "sample_network_5_updated"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|network                   |xsd:dict *(Required)*    |A ``network`` object.    |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the network, which is |
|                          |                         |up ( ``true`` ) or down  |
|                          |                         |( ``false`` ).           |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the network. |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The network name.        |
+--------------------------+-------------------------+-------------------------+
|shared                    |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |network is shared across |
|                          |                         |all tenants. By default, |
|                          |                         |only administrative      |
|                          |                         |users can change this    |
|                          |                         |value.                   |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The network status.      |
+--------------------------+-------------------------+-------------------------+
|subnets                   |xsd:list *(Required)*    |The associated subnets.  |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The UUID of the tenant.  |
+--------------------------+-------------------------+-------------------------+
|router:external           |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |network is externally    |
|                          |                         |accessible.              |
+--------------------------+-------------------------+-------------------------+
|mtu                       |xsd:int *(Required)*     |The MTU of a network     |
|                          |                         |resource.                |
+--------------------------+-------------------------+-------------------------+





**Example Update Network: JSON request**


.. code::

    {"network": {"status": "ACTIVE","subnets": [],"name": "sample_network_5_updated","provider:physical_network": null,"admin_state_up": true,"tenant_id": "4fd44f30292945e481c7b8a0c8908869","provider:network_type": "local","router:external": false,"mtu": 0,"shared": false,"port_security_enabled": true,"id": "1f370095-98f6-4079-be64-6d3d4a6adcc6","provider:segmentation_id": null}}

