=============================================================================
Unmanage Share -  OpenStack Compute API v2.1
=============================================================================

Unmanage Share
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_unmanage_share_v2_tenant_id_os-share-unmanage_share_id_unmanage.rst#request>`__
`Response <POST_unmanage_share_v2_tenant_id_os-share-unmanage_share_id_unmanage.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/os-share-unmanage/{share_id}/unmanage

Configures Shared File Systems to stop managing a share.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{share_id}                |csapi:UUID               |The UUID of the share.   |
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




