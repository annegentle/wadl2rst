=============================================================================
List Share Servers -  OpenStack Compute API v2.1
=============================================================================

List Share Servers
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_share_servers_v2_tenant_id_share-servers.rst#request>`__
`Response <GET_list_share_servers_v2_tenant_id_share-servers.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/share-servers

Lists all share servers.



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

+-------------------+-------------+---------------------------------------------+
|Name               |Type         |Description                                  |
+===================+=============+=============================================+
|id                 |csapi:UUID   |The share server ID.                         |
|                   |*(Required)* |                                             |
+-------------------+-------------+---------------------------------------------+
|project_id         |csapi:UUID   |The project ID.                              |
|                   |*(Required)* |                                             |
+-------------------+-------------+---------------------------------------------+
|status             |xsd:string   |The share server status, which is            |
|                   |*(Required)* |``active``, ``error``, ``creating``, or      |
|                   |             |``deleting``.                                |
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
|updated_at         |xsd:dateTime |The date and time stamp when the share       |
|                   |*(Required)* |server was updated. The date and time stamp  |
|                   |             |format is `ISO 8601                          |
|                   |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                   |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                   |             |value, if included, returns the time zone as |
|                   |             |an offset from UTC. For example, ``2015-08-  |
|                   |             |27T09:49:58-05:00``.                         |
+-------------------+-------------+---------------------------------------------+





**Example List Share Servers: JSON request**


.. code::

    {"share_servers": [{"status": "active","updated_at": "2015-09-07T08:52:15.000000","share_network_id": "713df749-aac0-4a54-af52-10f6c991e80c","host": "manila2@generic1","share_network_name": "net_my","project_id": "16e1ab15c35a457e9c2b2aa189f544e1","id": "ba11930a-bf1a-4aa7-bae4-a8dfbaa3cc73"}]}

