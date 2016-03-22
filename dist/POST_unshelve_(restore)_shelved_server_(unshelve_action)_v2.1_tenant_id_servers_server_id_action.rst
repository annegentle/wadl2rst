=============================================================================
Unshelve (Restore) Shelved Server (Unshelve Action) -  OpenStack Compute API v2.1
=============================================================================

Unshelve (Restore) Shelved Server (Unshelve Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_unshelve_(restore)_shelved_server_(unshelve_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_unshelve_(restore)_shelved_server_(unshelve_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Unshelves, or restores, a shelved server.

Specify the ``unshelve`` action in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.

Preconditions

The server status must be ``SHELVED`` or ``SHELVED_OFFLOADED``.

If the server is locked, you must have administrator privileges to unshelve the server.

Asynchronous Postconditions

After you successfully shelve a server, its status changes to ``ACTIVE``. The server appears on the compute node.

The shelved image is deleted from the list of images returned by an API call.

Troubleshooting

If the server status does not change to ``ACTIVE``, the unshelve operation failed. Ensure that you meet the preconditions and run the request again. If the request fails again, investigate whether another operation is running that causes a race condition.



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
|unshelve                  |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+





**Example Unshelve server: JSON request**


.. code::

    {
        "unshelve": null
    }
    


Response
^^^^^^^^^^^^^^^^^^




