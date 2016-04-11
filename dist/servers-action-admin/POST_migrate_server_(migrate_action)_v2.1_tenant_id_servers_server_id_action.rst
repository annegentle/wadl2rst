
Migrate Server (Migrate Action)
===============================

`Request <POST_migrate_server_(migrate_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_migrate_server_(migrate_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Migrates a server to a host. The scheduler chooses the host.

Specify the ``migrate`` action in the request body.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../migrateServer(MigrateAction).yaml

	- migrate: migrate




**Example Migrate Server (Migrate Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action-admin/migrate-req.json
   :language: javascript



Response
^^^^^^^^



