=============================================================================
List Share Networks -  OpenStack Compute API v2.1
=============================================================================

List Share Networks
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_share_networks_v2_tenant_id_share-networks.rst#request>`__
`Response <GET_list_share_networks_v2_tenant_id_share-networks.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/share-networks

Lists all share networks.



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

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |csapi:UUID *(Required)*  |The share network ID.    |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The share network name.  |
+--------------------------+-------------------------+-------------------------+





**Example List Share Networks: JSON request**


.. code::

    {"share_networks": [{"id": "32763294-e3d4-456a-998d-60047677c2fb","name": "net_my1"},{"id": "713df749-aac0-4a54-af52-10f6c991e80c","name": "net_my"},{"id": "fa158a3d-6d9f-4187-9ca5-abbb82646eb2","name": null}]}

