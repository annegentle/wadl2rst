=============================================================================
Resize Server -  OpenStack Compute API v2.1
=============================================================================

Resize Server
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_resize_server_v2_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_resize_server_v2_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/servers/{server_id}/action

Resizes a server.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|os-disk-config:diskConfig |                         |Valid value is ``AUTO``  |
|                          |                         |or ``MANUAL``.           |
+--------------------------+-------------------------+-------------------------+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+








**Example Resize Server: JSON request**


.. code::

    


Response
^^^^^^^^^^^^^^^^^^




