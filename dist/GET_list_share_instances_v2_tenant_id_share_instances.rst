=============================================================================
List Share Instances -  OpenStack Compute API v2.1
=============================================================================

List Share Instances
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_share_instances_v2_tenant_id_share_instances.rst#request>`__
`Response <GET_list_share_instances_v2_tenant_id_share_instances.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/share_instances

Lists all share instances.



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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+------------------+-------------+---------------------------------------------+
|Name              |Type         |Description                                  |
+==================+=============+=============================================+
|status            |xsd:string   |The share instance status. A valid value is  |
|                  |*(Required)* |``available``, ``error``, ``creating``,      |
|                  |             |``deleting``, and ``error_deleting``.        |
+------------------+-------------+---------------------------------------------+
|share_id          |csapi:UUID   |The UUID of the share from which the share   |
|                  |*(Required)* |instance was created.                        |
+------------------+-------------+---------------------------------------------+
|availability_zone |xsd:string   |The availability zone.                       |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|created_at        |xsd:dateTime |The date and time stamp when the share       |
|                  |*(Required)* |instance was created. The date and time      |
|                  |             |stamp format is `ISO 8601                    |
|                  |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                  |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                  |             |value, if included, returns the time zone as |
|                  |             |an offset from UTC. For example, ``2015-08-  |
|                  |             |27T09:49:58-05:00``.                         |
+------------------+-------------+---------------------------------------------+
|export_location   |xsd:string   |The share instance export location.          |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|export_locations  |xsd:list     |A list of share instance export locations.   |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|share_network_id  |csapi:UUID   |The share network ID.                        |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|host              |xsd:string   |The share instance host name.                |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+
|id                |csapi:UUID   |The share instance ID.                       |
|                  |*(Required)* |                                             |
+------------------+-------------+---------------------------------------------+





**Example List Share Instances: JSON request**


.. code::

    {"share_instances": [{"status": "error","share_id": "406ea93b-32e9-4907-a117-148b3945749f","availability_zone": "nova","created_at": "2015-09-07T08:41:20.000000","export_location": "10.254.0.3:/shares/share-081f7030-c54f-42f5-98ee-93a37393e0f2","share_network_id": "713df749-aac0-4a54-af52-10f6c991e80c","export_locations": ["10.254.0.3:/shares/share-081f7030-c54f-42f5-98ee-93a37393e0f2"],"share_server_id": "ba11930a-bf1a-4aa7-bae4-a8dfbaa3cc73","host": "manila2@generic1#GENERIC1","id": "081f7030-c54f-42f5-98ee-93a37393e0f2"},{"status": "available","share_id": "d94a8548-2079-4be0-b21c-0a887acd31ca","availability_zone": "nova","created_at": "2015-09-07T08:51:34.000000","export_location": "10.254.0.3:/shares/share-75559a8b-c90c-42a7-bda2-edbe86acfb7b","share_network_id": "713df749-aac0-4a54-af52-10f6c991e80c","export_locations": ["10.254.0.3:/shares/share-75559a8b-c90c-42a7-bda2-edbe86acfb7b"],"share_server_id": "ba11930a-bf1a-4aa7-bae4-a8dfbaa3cc73","host": "manila2@generic1#GENERIC1","id": "75559a8b-c90c-42a7-bda2-edbe86acfb7b"}]}

