=============================================================================
List Floating Ip Pools -  OpenStack Compute API v2.1
=============================================================================

List Floating Ip Pools
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_floating_ip_pools_v2.1_tenant_id_os-floating-ip-pools.rst#request>`__
`Response <GET_list_floating_ip_pools_v2.1_tenant_id_os-floating-ip-pools.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-floating-ip-pools

Lists floating IP pools.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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








Response
^^^^^^^^^^^^^^^^^^





**Example List Floating Ip Pools: JSON request**


.. code::

    {"floating_ip_pools": [{"name": "pool1"},{"name": "pool2"}]}

