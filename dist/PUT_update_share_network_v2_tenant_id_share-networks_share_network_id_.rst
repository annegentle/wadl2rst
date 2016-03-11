=============================================================================
Update Share Network -  OpenStack Compute API v2.1
=============================================================================

Update Share Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_share_network_v2_tenant_id_share-networks_share_network_id_.rst#request>`__
`Response <PUT_update_share_network_v2_tenant_id_share-networks_share_network_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/share-networks/{share_network_id}

Updates a share network.

Note that if the share network is used by any share server, you can update only the ``name`` and ``description`` attributes.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The share network name.  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The share network        |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+





**Example Update Share Network: JSON request**


.. code::

    {"share_network": {"description": "i'm adding a description"}}


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





**Example Update Share Network: JSON request**


.. code::

    {"share_network": {"name": "net_my","segmentation_id": null,"created_at": "2015-09-04T14:54:25.000000","neutron_subnet_id": "53482b62-2c84-4a53-b6ab-30d9d9800d06","updated_at": "2015-09-07T08:02:53.512184","id": "713df749-aac0-4a54-af52-10f6c991e80c","neutron_net_id": "998b42ee-2cee-4d36-8b95-67b5ca1f2109","ip_version": "4","nova_net_id": null,"cidr": null,"project_id": "16e1ab15c35a457e9c2b2aa189f544e1","network_type": null,"description": "i'm adding a description"}}

