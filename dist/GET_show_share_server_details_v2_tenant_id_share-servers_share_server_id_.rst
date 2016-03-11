=============================================================================
Show Share Server Details -  OpenStack Compute API v2.1
=============================================================================

Show Share Server Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_share_server_details_v2_tenant_id_share-servers_share_server_id_.rst#request>`__
`Response <GET_show_share_server_details_v2_tenant_id_share-servers_share_server_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/share-servers/{share_server_id}

Shows details for a share server.



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
|{share_server_id}         |csapi:UUID               |The UUID of the share    |
|                          |                         |server.                  |
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

+-------------------+-------------+---------------------------------------------+
|Name               |Type         |Description                                  |
+===================+=============+=============================================+
|id                 |csapi:UUID   |The share server ID.                         |
|                   |*(Required)* |                                             |
+-------------------+-------------+---------------------------------------------+
|project_id         |csapi:UUID   |The project ID.                              |
|                   |*(Required)* |                                             |
+-------------------+-------------+---------------------------------------------+
|status             |xsd:string   |The share server status, which is is         |
|                   |*(Required)* |``active``, ``error``, ``creating``, or      |
|                   |             |``deleting``.                                |
+-------------------+-------------+---------------------------------------------+
|backend_details    |xsd:dict     |The back-end details for a server. Each back |
|                   |*(Required)* |end can store any key-value information that |
|                   |             |it requires. For example, the generic back-  |
|                   |             |end driver might store the router ID.        |
+-------------------+-------------+---------------------------------------------+
|share_network_id   |csapi:UUID   |The UUID of a share network that is          |
|                   |*(Required)* |associated with the share server.            |
+-------------------+-------------+---------------------------------------------+
|share_network_name |xsd:string   |The name of a share network that is          |
|                   |*(Required)* |associated with the share server.            |
+-------------------+-------------+---------------------------------------------+
|host               |xsd:string   |The share server host name or IP address.    |
|                   |*(Required)* |                                             |
+-------------------+-------------+---------------------------------------------+
|created_at         |xsd:dateTime |The date and time stamp when the share       |
|                   |*(Required)* |server was created. The date and time stamp  |
|                   |             |format is `ISO 8601                          |
|                   |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                   |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                   |             |value, if included, returns the time zone as |
|                   |             |an offset from UTC. For example, ``2015-08-  |
|                   |             |27T09:49:58-05:00``.                         |
+-------------------+-------------+---------------------------------------------+
|updated_at         |xsd:dateTime |The date and time stamp when the share       |
|                   |*(Required)* |server was updated. The date and time stamp  |
|                   |             |format is `ISO 8601                          |
|                   |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                   |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                   |             |value, if included, returns the time zone as |
|                   |             |an offset from UTC. For example, ``2015-08-  |
|                   |             |27T09:49:58-05:00``.                         |
+-------------------+-------------+---------------------------------------------+





**Example Show Share Server Details: JSON request**


.. code::

    {"share_server": {"status": "active","backend_details": {"username": "manila","router_id": "4b62ce91-56c5-45c1-b0ef-8cbbe5dd34f4","pk_path": "/opt/stack/.ssh/id_rsa","subnet_id": "16e99ad6-5191-461c-9f34-ac84a39c3adb","ip": "10.254.0.3","instance_id": "75f2f282-af65-49ba-a7b1-525705b1bf1a","public_address": "10.254.0.3","service_port_id": "8ff21760-961e-4b83-a032-03fd559bb1d3"},"created_at": "2015-09-07T08:37:19.000000","updated_at": "2015-09-07T08:52:15.000000","share_network_name": "net_my","host": "manila2@generic1","share_network_id": "713df749-aac0-4a54-af52-10f6c991e80c","project_id": "16e1ab15c35a457e9c2b2aa189f544e1","id": "ba11930a-bf1a-4aa7-bae4-a8dfbaa3cc73"}}

