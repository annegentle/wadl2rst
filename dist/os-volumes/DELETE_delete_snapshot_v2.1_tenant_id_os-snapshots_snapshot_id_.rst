
Delete Snapshot
===============

`Request <DELETE_delete_snapshot_v2.1_tenant_id_os-snapshots_snapshot_id_.rst#request>`__
`Response <DELETE_delete_snapshot_v2.1_tenant_id_os-snapshots_snapshot_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/os-snapshots/{snapshot_id}

Deletes a snapshot from the account.

This operation is asynchronous. You must list snapshots repeatedly to determine whether the snapshot was deleted.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Delete Snapshot: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/snapshot-delete-json-http.txt
   :language: javascript

