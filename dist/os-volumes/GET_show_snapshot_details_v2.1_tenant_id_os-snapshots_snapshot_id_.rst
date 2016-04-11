
Show Snapshot Details
=====================

`Request <GET_show_snapshot_details_v2.1_tenant_id_os-snapshots_snapshot_id_.rst#request>`__
`Response <GET_show_snapshot_details_v2.1_tenant_id_os-snapshots_snapshot_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-snapshots/{snapshot_id}

Shows details for a snapshot.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Snapshot Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/snapshot-show-resp.json
   :language: javascript

