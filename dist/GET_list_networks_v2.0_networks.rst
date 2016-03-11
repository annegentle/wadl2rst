=============================================================================
List Networks -  OpenStack Compute API v2.1
=============================================================================

List Networks
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_networks_v2.0_networks.rst#request>`__
`Response <GET_list_networks_v2.0_networks.rst#response>`__

.. code-block:: javascript

    GET /v2.0/networks

Lists networks to which the tenant has access.

Use the ``fields`` query parameter to filter the response. For information, see `Filtering and Column Selection <https://wiki.openstack.org/wiki/Neutron/APIv2-specification#Filtering_and_Column_Selection>`__.



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





**Example List Networks: JSON request**


.. code::

    {"networks": [{"status": "ACTIVE","subnets": ["54d6f61d-db07-451c-9ab3-b9609b6b6f0b"],"name": "private-network","provider:physical_network": null,"admin_state_up": true,"tenant_id": "4fd44f30292945e481c7b8a0c8908869","provider:network_type": "local","router:external": true,"mtu": 0,"shared": true,"id": "d32019d3-bc6e-4319-9c1d-6722fc136a22","provider:segmentation_id": null},{"status": "ACTIVE","subnets": ["08eae331-0402-425a-923c-34f7cfe39c1b"],"name": "private","provider:physical_network": null,"admin_state_up": true,"tenant_id": "26a7980765d0414dbc1fc1f88cdb7e6e","provider:network_type": "local","router:external": true,"mtu": 0,"shared": true,"id": "db193ab3-96e3-4cb3-8fc5-05f4296d0324","provider:segmentation_id": null}]}

