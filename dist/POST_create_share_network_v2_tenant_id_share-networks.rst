=============================================================================
Create Share Network -  OpenStack Compute API v2.1
=============================================================================

Create Share Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_share_network_v2_tenant_id_share-networks.rst#request>`__
`Response <POST_create_share_network_v2_tenant_id_share-networks.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/share-networks

Creates a share network.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|X-Openstack-Manila-Api-   |xsd:string               |The HTTP header to       |
|Version                   |                         |specify a valid Shared   |
|                          |                         |File Systems API micro-  |
|                          |                         |version. For example,    |
|                          |                         |``"X-Openstack-Manila-   |
|                          |                         |Api-Version: 2.6"``. If  |
|                          |                         |you omit this header,    |
|                          |                         |the default micro-       |
|                          |                         |version is 2.0.          |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|neutron_net_id            |csapi:UUID *(Required)*  |The UUID of the neutron  |
|                          |                         |network to set up for    |
|                          |                         |share servers. You can   |
|                          |                         |set up either a neutron  |
|                          |                         |network and subnet or a  |
|                          |                         |nova network.            |
+--------------------------+-------------------------+-------------------------+
|neutron_subnet_id         |csapi:UUID *(Required)*  |The UUID of the neutron  |
|                          |                         |subnet to set up for     |
|                          |                         |share servers. This      |
|                          |                         |subnet must be part of   |
|                          |                         |the neutron network. You |
|                          |                         |can set up either a      |
|                          |                         |neutron network and      |
|                          |                         |subnet or a nova network.|
+--------------------------+-------------------------+-------------------------+
|nova_net_id               |csapi:UUID *(Required)*  |The UUID of the nova     |
|                          |                         |network to set up for    |
|                          |                         |share servers. You can   |
|                          |                         |set up either a neutron  |
|                          |                         |network and subnet or a  |
|                          |                         |nova network.            |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The share network name.  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The share network        |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+





**Example Create Share Network: JSON request**


.. code::

    {"share_network": {"neutron_net_id": "998b42ee-2cee-4d36-8b95-67b5ca1f2109","neutron_subnet_id": "53482b62-2c84-4a53-b6ab-30d9d9800d06","name": "my_network","description": "This is my share network"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+------------------+-------------+---------------------------------------------+
|Name              |Type         |Description                                  |
+==================+=============+=============================================+
|id                |csapi:UUID   |The share network ID.                        |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|project_id        |csapi:UUID   |The UUID of the project where the share      |
|                  |*(Required)* |network was created.                         |
+------------------+-------------+---------------------------------------------+
|neutron_net_id    |csapi:UUID   |The neutron network ID.                      |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|neutron_subnet_id |csapi:UUID   |The neutron subnet ID.                       |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|nova_net_id       |csapi:UUID   |The nova network ID.                         |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|network_type      |xsd:string   |The network type. A valid value is ``VLAN``, |
|                  |*(Required)* |``VXLAN``, ``GRE``, or ``flat``. This        |
|                  |             |parameter is automatically set to a value    |
|                  |             |determined by the network provider.          |
+------------------+-------------+---------------------------------------------+
|segmentation_id   |xsd:int      |The segmentation ID. This parameter is       |
|                  |*(Required)* |automatically set to a value determined by   |
|                  |             |the network provider. For VLAN, this value   |
|                  |             |is an integer from 1 to 4094. For VXLAN,     |
|                  |             |this value is an integer from 1 to 16777215. |
|                  |             |For GRE, this value is an integer from 1 to  |
|                  |             |4294967295.                                  |
+------------------+-------------+---------------------------------------------+
|cidr              |xsd:string   |The IP block from which to allocate the      |
|                  |*(Required)* |network, in CIDR notation. For example,      |
|                  |             |``172.16.0.0/24`` or ``2001:DB8::/64``. This |
|                  |             |parameter is automatically set to a value    |
|                  |             |determined by the network provider.          |
+------------------+-------------+---------------------------------------------+
|ip_version        |xsd:int      |The IP version of the network. A valid value |
|                  |*(Required)* |is ``4`` or ``6``. This parameter is         |
|                  |             |automatically set to a value determined by   |
|                  |             |the network provider.                        |
+------------------+-------------+---------------------------------------------+
|name              |xsd:string   |The share network name.                      |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|description       |xsd:string   |The share network description.               |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|created_at        |xsd:dateTime |The date and time stamp when the share       |
|                  |*(Required)* |network was created. The date and time stamp |
|                  |             |format is `ISO 8601                          |
|                  |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                  |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                  |             |value, if included, returns the time zone as |
|                  |             |an offset from UTC. For example, ``2015-08-  |
|                  |             |27T09:49:58-05:00``.                         |
+------------------+-------------+---------------------------------------------+
|updated_at        |xsd:dateTime |The date and time stamp when the share       |
|                  |*(Required)* |network was updated. The date and time stamp |
|                  |             |format is `ISO 8601                          |
|                  |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                  |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                  |             |value, if included, returns the time zone as |
|                  |             |an offset from UTC. For example, ``2015-08-  |
|                  |             |27T09:49:58-05:00``.                         |
+------------------+-------------+---------------------------------------------+





**Example Create Share Network: JSON request**


.. code::

    {"share_network": {"name": "my_network","segmentation_id": null,"created_at": "2015-09-07T14:37:00.583656","neutron_subnet_id": "53482b62-2c84-4a53-b6ab-30d9d9800d06","updated_at": null,"id": "77eb3421-4549-4789-ac39-0d5185d68c29","neutron_net_id": "998b42ee-2cee-4d36-8b95-67b5ca1f2109","ip_version": null,"nova_net_id": null,"cidr": null,"project_id": "e10a683c20da41248cfd5e1ab3d88c62","network_type": null,"description": "This is my share network"}}

