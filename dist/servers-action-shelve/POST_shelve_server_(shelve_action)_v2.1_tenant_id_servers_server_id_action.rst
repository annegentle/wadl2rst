
Shelve Server (Shelve Action)
=============================

`Request <POST_shelve_server_(shelve_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_shelve_server_(shelve_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Shelves a server.

Specify the ``shelve`` action in the request body.

All associated data and resources are kept but anything still in memory is not retained. To restore a shelved instance, use the ``unshelve`` action. To remove a shelved instance, use the ``shelveOffload`` action.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.

Preconditions

The server status must be ``ACTIVE``, ``SHUTOFF``, ``PAUSED``, or ``SUSPENDED``.

If the server is locked, you must have administrator privileges to shelve the server.

Asynchronous Postconditions

After you successfully shelve a server, its status changes to ``SHELVED`` and the image status is ``ACTIVE``. The server instance data appears on the compute node that the Compute service manages.

If you boot the server from volumes or set the ``shelved_offload_time`` option to 0, the Compute service automatically deletes the instance on compute nodes and changes the server status to ``SHELVED_OFFLOADED``.

Troubleshooting

If the server status does not change to ``SHELVED`` or ``SHELVED_OFFLOADED``, the shelve operation failed. Ensure that you meet the preconditions and run the request again. If the request fails again, investigate whether another operation is running that causes a race condition.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../shelveServer(ShelveAction).yaml

	- shelve: shelve




**Example Shelve server: JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action/shelve-req.json
   :language: javascript



Response
^^^^^^^^



