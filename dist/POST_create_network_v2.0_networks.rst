=============================================================================
Create Network -  OpenStack Compute API v2.1
=============================================================================

Create Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_network_v2.0_networks.rst#request>`__
`Response <POST_create_network_v2.0_networks.rst#response>`__

.. code-block:: javascript

    POST /v2.0/networks

Creates a network.

A request body is optional. An administrative user can specify another tenant UUID, which is the tenant who owns the network, in the request body.



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
|network                   |xsd:dict *(Required)*    |A ``network`` object.    |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the network, which is |
|                          |                         |up ( ``true`` ) or down  |
|                          |                         |( ``false`` ).           |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The network name. A      |
|                          |                         |request body is          |
|                          |                         |optional: If you include |
|                          |                         |it, it can specify this  |
|                          |                         |optional attribute.      |
+--------------------------+-------------------------+-------------------------+
|shared                    |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |network is shared across |
|                          |                         |all tenants. By default, |
|                          |                         |only administrative      |
|                          |                         |users can change this    |
|                          |                         |value.                   |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |Admin-only. The UUID of  |
|                          |                         |the tenant that owns the |
|                          |                         |network. This tenant can |
|                          |                         |be different from the    |
|                          |                         |tenant that makes the    |
|                          |                         |create network request.  |
|                          |                         |However, only            |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
|                          |                         |You cannot change this   |
|                          |                         |value through            |
|                          |                         |authorization policies.  |
+--------------------------+-------------------------+-------------------------+
|router:external           |xsd:bool *(Required)*    |Indicates whether this   |
|                          |                         |network is externally    |
|                          |                         |accessible.              |
+--------------------------+-------------------------+-------------------------+





**Example Create Network: JSON request**


.. code::

    {"network": {"name": "sample_network","admin_state_up": true}}


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





**Example Create Network: JSON request**


.. code::

    {"network": {"status": "ACTIVE","subnets": [],"name": "net1","admin_state_up": true,"tenant_id": "9bacb3c5d39d41a79512987f338cf177","router:external": false,"mtu": 0,"shared": false,"id": "4e8e5957-649f-477b-9e5b-f1f75b21c03c"}}

