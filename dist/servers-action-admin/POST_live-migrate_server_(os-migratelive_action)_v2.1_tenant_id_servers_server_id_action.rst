
Live-Migrate Server (Os-Migratelive Action)
===========================================

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Live-migrates a server to a new host without rebooting.

Use the ``host`` parameter to specify the destination host. If you omit this parameter, the scheduler chooses a host. If a scheduled host is not suitable, the scheduler tries up to ``migrate_max_retries`` rescheduling attempts.

If both source and destination hosts provide local disks, you can set the ``block_migration`` parameter to ``true``. If either host uses shared storage, the migration fails if you set this parameter to ``true``.

Policy defaults enable only users with the administrative role to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 202

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../live-migrateServer(Os-MigrateliveAction).yaml

	- tenant_id: tenant_id
	- server_id: server_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../live-migrateServer(Os-MigrateliveAction).yaml

	- host: host
	- block_migration: block_migration
	- disk_over_commit: disk_over_commit




**Example Live-Migrate Server (Os-Migratelive Action): JSON request**


.. literalinclude:: ../../../doc/api_samples/servers-action-admin/os-migrateLive-req.json
   :language: javascript



Response
^^^^^^^^




