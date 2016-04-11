
Delete Snapshot
===============

.. rest_method:: DELETE /v2.1/{tenant_id}/os-snapshots/{snapshot_id}

Deletes a snapshot from the account.

This operation is asynchronous. You must list snapshots repeatedly to determine whether the snapshot was deleted.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteSnapshot.yaml

	- tenant_id: tenant_id
	- snapshot_id: snapshot_id








Response
^^^^^^^^





**Example Delete Snapshot: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/snapshot-delete-json-http.txt
   :language: javascript


