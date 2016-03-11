=============================================================================
Show Network Details -  OpenStack Compute API v2.1
=============================================================================

Show Network Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_network_details_v2.0_networks_network_id_.rst#request>`__
`Response <GET_show_network_details_v2.0_networks_network_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.0/networks/{network_id}

Shows details for a network.

You can control which response parameters are returned by using the fields query parameter. For information, see `Filtering and column selection <http://specs.openstack.org/openstack/neutron-specs/specs/api/networking_general_api_information.html#filtering-and-column-selection>`__.

The response might show extension response parameters. For information, see `Networks multiple provider extension (networks) <http://developer.openstack.org/api-ref-networking-v2-ext.html#showProviderNetwork>`__.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
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
|{network_id}              |csapi:UUID *(Required)*  |The UUID of the network. |
+--------------------------+-------------------------+-------------------------+








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





**Example Show Network Details: JSON request**


.. code::

    {"network": {"status": "ACTIVE","subnets": ["54d6f61d-db07-451c-9ab3-b9609b6b6f0b"],"name": "private-network","router:external": false,"admin_state_up": true,"tenant_id": "4fd44f30292945e481c7b8a0c8908869","mtu": 0,"shared": true,"port_security_enabled": true,"id": "d32019d3-bc6e-4319-9c1d-6722fc136a22"}}

