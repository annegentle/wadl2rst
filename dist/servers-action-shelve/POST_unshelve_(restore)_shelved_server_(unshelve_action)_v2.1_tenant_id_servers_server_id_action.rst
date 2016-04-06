
Unshelve (Restore) Shelved Server (Unshelve Action)
===================================================

`Request <POST_unshelve_(restore)_shelved_server_(unshelve_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_unshelve_(restore)_shelved_server_(unshelve_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

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



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- server_id: server_id




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
^^^^^^^^




