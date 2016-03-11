=============================================================================
List Share Snapshots -  OpenStack Compute API v2.1
=============================================================================

List Share Snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_share_snapshots_v2_tenant_id_snapshots.rst#request>`__
`Response <GET_list_share_snapshots_v2_tenant_id_snapshots.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/snapshots

Lists all share snapshots.



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
|id                        |csapi:UUID *(Required)*  |The UUID of the snapshot.|
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The snapshot name.       |
+--------------------------+-------------------------+-------------------------+





**Example List Share Snapshots: JSON request**


.. code::

    {"snapshots": [{"id": "086a1aa6-c425-4ecd-9612-391a3b1b9375","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/086a1aa6-c425-4ecd-9612-391a3b1b9375","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/086a1aa6-c425-4ecd-9612-391a3b1b9375","rel": "bookmark"}],"name": "snapshot_My_share"},{"id": "6d221c1d-0200-461e-8d20-24b4776b9ddb","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "bookmark"}],"name": "snapshot_share1"}]}

