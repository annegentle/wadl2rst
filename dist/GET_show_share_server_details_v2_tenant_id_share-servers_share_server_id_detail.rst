=============================================================================
Show Share Server Details -  OpenStack Compute API v2.1
=============================================================================

Show Share Server Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_share_server_details_v2_tenant_id_share-servers_share_server_id_detail.rst#request>`__
`Response <GET_show_share_server_details_v2_tenant_id_share-servers_share_server_id_detail.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/share-servers/{share_server_id}/detail

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

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|backend_details           |xsd:string *(Required)*  |The back-end details for |
|                          |                         |a server. Each back end  |
|                          |                         |can store any key-value  |
|                          |                         |information that it      |
|                          |                         |requires. For example,   |
|                          |                         |the generic back-end     |
|                          |                         |driver might store the   |
|                          |                         |router ID.               |
+--------------------------+-------------------------+-------------------------+





**Example Show Share Server Details: JSON request**


.. code::

    {"details": {"username": "manila","router_id": "4b62ce91-56c5-45c1-b0ef-8cbbe5dd34f4","pk_path": "/opt/stack/.ssh/id_rsa","subnet_id": "16e99ad6-5191-461c-9f34-ac84a39c3adb","ip": "10.254.0.3","instance_id": "75f2f282-af65-49ba-a7b1-525705b1bf1a","public_address": "10.254.0.3","service_port_id": "8ff21760-961e-4b83-a032-03fd559bb1d3"}}

