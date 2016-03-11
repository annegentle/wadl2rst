=============================================================================
List Back-End Storage Pools -  OpenStack Compute API v2.1
=============================================================================

List Back-End Storage Pools
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_back-end_storage_pools_v2_tenant_id_scheduler-stats_pools.rst#request>`__
`Response <GET_list_back-end_storage_pools_v2_tenant_id_scheduler-stats_pools.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/scheduler-stats/pools

Lists all back-end storage pools.



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
|backend                   |xsd:string *(Required)*  |The name of the back end.|
+--------------------------+-------------------------+-------------------------+
|host                      |xsd:string *(Required)*  |The host name for the    |
|                          |                         |back end.                |
+--------------------------+-------------------------+-------------------------+
|pool                      |xsd:string *(Required)*  |The pool name for the    |
|                          |                         |back end.                |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name of the back end |
|                          |                         |in this format:          |
|                          |                         |``host@backend#POOL``.   |
|                          |                         |``host``. The host name  |
|                          |                         |for the back end.        |
|                          |                         |``backend``. The name of |
|                          |                         |the back end. ``POOL``.  |
|                          |                         |The pool name for the    |
|                          |                         |back end.                |
+--------------------------+-------------------------+-------------------------+





**Example List Back-End Storage Pools: JSON request**


.. code::

    {"pools": [{"host": "manila2","name": "manila2@generic1#GENERIC1","pool": "GENERIC1","backend": "generic1"},{"host": "manila2","name": "manila2@unmanage1#UNMANAGE1","pool": "UNMANAGE1","backend": "unmanage1"},{"host": "manila2","name": "manila2@ams_backend#AMS_BACKEND","pool": "AMS_BACKEND","backend": "ams_backend"}]}

