
Shelf-Offload (Remove) Server (Shelveoffload Action)
====================================================

`Request <POST_shelf-offload_(remove)_server_(shelveoffload_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_shelf-offload_(remove)_server_(shelveoffload_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Shelf-offloads, or removes, a shelved server.

Specify the ``shelveOffload`` action in the request body.

Data and resource associations are deleted. If an instance is no longer needed, you can remove that instance from the hypervisor to minimize resource usage.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.

Preconditions

The server status must be ``SHELVED``.

If the server is locked, you must have administrator privileges to shelve-offload the server.

Asynchronous Postconditions

After you successfully shelve-offload a server, its status changes to ``SHELVED_OFFLOADED``. The server instance data appears on the compute node.

Troubleshooting

If the server status does not change to ``SHELVED_OFFLOADED``, the shelve-offload operation failed. Ensure that you meet the preconditions and run the request again. If the request fails again, investigate whether another operation is running that causes a race condition.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: shelf-offload(Remove)Server(ShelveoffloadAction).yaml

	- shelveOffload: shelveOffload




**Example Shelve server: JSON request**


.. code::

    {
        "shelveOffload": null
    }
    


Response
^^^^^^^^




