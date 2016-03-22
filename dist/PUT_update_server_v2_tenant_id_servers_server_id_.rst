=============================================================================
Update Server -  OpenStack Compute API v2.1
=============================================================================

Update Server
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_server_v2_tenant_id_servers_server_id_.rst#request>`__
`Response <PUT_update_server_v2_tenant_id_servers_server_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/servers/{server_id}

Updates a server.



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
|os-disk-config:diskConfig |                         |Valid value is ``AUTO``  |
|                          |                         |or ``MANUAL``.           |
+--------------------------+-------------------------+-------------------------+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+








**Example Update Server: JSON request**


.. code::

    


Response
^^^^^^^^^^^^^^^^^^





**Example Update Server: JSON request**


.. code::

    

