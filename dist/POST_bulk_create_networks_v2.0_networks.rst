=============================================================================
Bulk Create Networks -  OpenStack Compute API v2.1
=============================================================================

Bulk Create Networks
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_bulk_create_networks_v2.0_networks.rst#request>`__
`Response <POST_bulk_create_networks_v2.0_networks.rst#response>`__

.. code-block:: javascript

    POST /v2.0/networks

Creates multiple networks in a single request.

In the request body, specify a list of networks.

The bulk create operation is always atomic. Either all or no networks in the request body are created.



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
|networks                  |xsd:list *(Required)*    |A list of ``network``    |
|                          |                         |objects.                 |
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
|router:external           |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |network is externally    |
|                          |                         |accessible.              |
+--------------------------+-------------------------+-------------------------+
|port_security_enabled     |xsd:boolean *(Required)* |The port security        |
|                          |                         |status. A valid value is |
|                          |                         |enabled ( ``true`` ) or  |
|                          |                         |disabled ( ``false`` ).  |
+--------------------------+-------------------------+-------------------------+





**Example Bulk Create Networks: JSON request**


.. code::

    {"networks": [{"name": "sample_network3","admin_state_up": true},{"name": "sample_network4","admin_state_up": true}]}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|networks                  |xsd:list *(Required)*    |A list of ``network``    |
|                          |                         |objects.                 |
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
|                          |                         |all tenants.             |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The network status.      |
+--------------------------+-------------------------+-------------------------+
|subnets                   |xsd:list *(Required)*    |The associated subnets.  |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The UUID of the tenant   |
|                          |                         |who owns the network.    |
+--------------------------+-------------------------+-------------------------+
|router:external           |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |network is externally    |
|                          |                         |accessible.              |
+--------------------------+-------------------------+-------------------------+
|mtu                       |xsd:int *(Required)*     |The MTU of a network     |
|                          |                         |resource.                |
+--------------------------+-------------------------+-------------------------+
|port_security_enabled     |xsd:boolean *(Required)* |The port security        |
|                          |                         |status. A valid value is |
|                          |                         |enabled ( ``true`` ) or  |
|                          |                         |disabled ( ``false`` ).  |
+--------------------------+-------------------------+-------------------------+





**Example Bulk Create Networks: JSON request**


.. code::

    {"networks": [{"status": "ACTIVE","subnets": [],"name": "sample_network3","provider:physical_network": null,"admin_state_up": true,"tenant_id": "4fd44f30292945e481c7b8a0c8908869","mtu": 0,"shared": false,"id": "bc1a76cb-8767-4c3a-bb95-018b822f2130","provider:segmentation_id": null},{"status": "ACTIVE","subnets": [],"name": "sample_network4","provider:physical_network": null,"admin_state_up": true,"tenant_id": "4fd44f30292945e481c7b8a0c8908869","mtu": 0,"shared": false,"id": "af374017-c9ae-4a1d-b799-ab73111476e2","provider:segmentation_id": null}]}

