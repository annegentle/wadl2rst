
Show Snapshot Details
=====================

.. rest_method:: GET /v2.1/{tenant_id}/os-snapshots/{snapshot_id}

Shows details for a snapshot.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showSnapshotDetails.yaml

	- tenant_id: tenant_id
	- snapshot_id: snapshot_id








Response
^^^^^^^^





**Example Show Snapshot Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/snapshot-show-resp.json
   :language: javascript


