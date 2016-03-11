=============================================================================
Show Share Network Details -  OpenStack Compute API v2.1
=============================================================================

Show Share Network Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_share_network_details_v2_tenant_id_share-networks_share_network_id_.rst#request>`__
`Response <GET_show_share_network_details_v2_tenant_id_share-networks_share_network_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/share-networks/{share_network_id}

Shows details for a share network.



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
|{share_network_id}        |csapi:UUID               |The UUID of the share    |
|                          |                         |network.                 |
+--------------------------+-------------------------+-------------------------+
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
|                  |*(Required)* |``VXLAN``, ``GRE``, or ``flat``.             |
+------------------+-------------+---------------------------------------------+
|segmentation_id   |xsd:int      |The segmentation ID.                         |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|cidr              |xsd:string   |The CIDR.                                    |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|ip_version        |xsd:int      |The IP version of the network. A valid value |
|                  |*(Required)* |is ``4`` or ``6``.                           |
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





**Example Show Share Network Details: JSON request**


.. code::

    {"share_network": {"name": "net_my1","segmentation_id": null,"created_at": "2015-09-04T14:56:45.000000","neutron_subnet_id": "53482b62-2c84-4a53-b6ab-30d9d9800d06","updated_at": null,"id": "7f950b52-6141-4a08-bbb5-bb7ffa3ea5fd","neutron_net_id": "998b42ee-2cee-4d36-8b95-67b5ca1f2109","ip_version": null,"nova_net_id": null,"cidr": null,"project_id": "16e1ab15c35a457e9c2b2aa189f544e1","network_type": null,"description": "descr"}}

