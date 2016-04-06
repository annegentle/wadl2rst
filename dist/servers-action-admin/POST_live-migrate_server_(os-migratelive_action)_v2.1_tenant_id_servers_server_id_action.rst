
Live-Migrate Server (Os-Migratelive Action)
===========================================

`Request <POST_live-migrate_server_(os-migratelive_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_live-migrate_server_(os-migratelive_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Live-migrates a server to a new host without rebooting.

Use the ``host`` parameter to specify the destination host. If you omit this parameter, the scheduler chooses a host. If a scheduled host is not suitable, the scheduler tries up to ``migrate_max_retries`` rescheduling attempts.

If both source and destination hosts provide local disks, you can set the ``block_migration`` parameter to ``True``. If either host uses shared storage, the migration fails if you set this parameter to ``True``.

Policy defaults enable only users with the administrative role to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
|host                      |xsd:string *(Required)*  |The host to which to     |
|                          |                         |migrate the server. If   |
|                          |                         |you omit this parameter, |
|                          |                         |the scheduler chooses a  |
|                          |                         |host.                    |
+--------------------------+-------------------------+-------------------------+
|block_migration           |xsd:boolean *(Required)* |Set to ``True`` to       |
|                          |                         |migrate local disks by   |
|                          |                         |using block migration.   |
|                          |                         |If the source or         |
|                          |                         |destination host uses    |
|                          |                         |shared storage and you   |
|                          |                         |set this value to        |
|                          |                         |``True``, the live       |
|                          |                         |migration fails.         |
+--------------------------+-------------------------+-------------------------+
|disk_over_commit          |xsd:boolean *(Required)* |Set to ``True`` to       |
|                          |                         |enable over commit when  |
|                          |                         |the destination host is  |
|                          |                         |checked for available    |
|                          |                         |disk space. Set to       |
|                          |                         |``False`` to disable     |
|                          |                         |over commit. This        |
|                          |                         |setting affects only the |
|                          |                         |libvirt virt driver.     |
+--------------------------+-------------------------+-------------------------+





**Example Live-Migrate Server (Os-Migratelive Action): JSON request**


.. code::

    {
        "os-migrateLive": {
            "host": "01c0cadef72d47e28a672a76060d492c",
            "block_migration": false,
            "disk_over_commit": false
        }
    }
    


Response
^^^^^^^^




