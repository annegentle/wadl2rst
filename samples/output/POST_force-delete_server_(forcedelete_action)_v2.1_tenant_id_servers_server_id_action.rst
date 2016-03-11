=============================================================================
Force-Delete Server (Forcedelete Action) -  OpenStack Compute API v2.1
=============================================================================

Force-Delete Server (Forcedelete Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_force-delete_server_(forcedelete_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_force-delete_server_(forcedelete_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Force-deletes a server before deferred cleanup.

Specify the ``forceDelete`` action in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|forceDelete               |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Force-Delete Server (Forcedelete Action): JSON request**


.. code::

    {
        "forceDelete": null
    }
    


Response
^^^^^^^^^^^^^^^^^^




