
Create Snapshot
===============

`Request <POST_create_snapshot_v2.1_tenant_id_os-snapshots.rst#request>`__
`Response <POST_create_snapshot_v2.1_tenant_id_os-snapshots.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-snapshots

Creates a snapshot.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../createSnapshot.yaml

	- snapshot: snapshot




**Example Create Snapshot: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/snapshot-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Snapshot: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/snapshot-show-resp.json
   :language: javascript

