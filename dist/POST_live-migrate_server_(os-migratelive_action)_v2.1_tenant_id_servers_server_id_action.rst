=============================================================================
Live-Migrate Server (Os-Migratelive Action) -  OpenStack Compute API v2.1
=============================================================================

Live-Migrate Server (Os-Migratelive Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_live-migrate_server_(os-migratelive_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_live-migrate_server_(os-migratelive_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Live-migrates a server to a new host without rebooting.

Use the ``host`` parameter to specify the destination host. If you omit this parameter, the scheduler chooses a host. If a scheduled host is not suitable, the scheduler tries up to ``migrate_max_retries`` rescheduling attempts.

If both source and destination hosts provide local disks, you can set the ``block_migration`` parameter to ``True``. If either host uses shared storage, the migration fails if you set this parameter to ``True``.

Policy defaults enable only users with the administrative role to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
^^^^^^^^^^^^^^^^^^




