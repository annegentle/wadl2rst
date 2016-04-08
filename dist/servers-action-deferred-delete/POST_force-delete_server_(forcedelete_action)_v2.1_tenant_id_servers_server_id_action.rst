
Force-Delete Server (Forcedelete Action)
========================================

`Request <POST_force-delete_server_(forcedelete_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_force-delete_server_(forcedelete_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Force-deletes a server before deferred cleanup.

Specify the ``forceDelete`` action in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: force-deleteServer(ForcedeleteAction).yaml

	- forceDelete: forceDelete




**Example Force-Delete Server (Forcedelete Action): JSON request**


.. code::

    {
        "forceDelete": null
    }
    


Response
^^^^^^^^




