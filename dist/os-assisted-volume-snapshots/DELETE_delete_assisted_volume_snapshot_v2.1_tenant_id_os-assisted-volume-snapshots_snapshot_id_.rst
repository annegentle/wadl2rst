
Delete Assisted Volume Snapshot
===============================

`Request <DELETE_delete_assisted_volume_snapshot_v2.1_tenant_id_os-assisted-volume-snapshots_snapshot_id_.rst#request>`__
`Response <DELETE_delete_assisted_volume_snapshot_v2.1_tenant_id_os-assisted-volume-snapshots_snapshot_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/os-assisted-volume-snapshots/{snapshot_id}

Deletes an assisted volume snapshot.

To make this request, add the ``delete_info`` query parameter to the URI, as follows:

DELETE /os-assisted-volume-snapshots?delete_info='{"volume_id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c"}'

Normal response codes: 204

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


.. rest_parameters:: ../deleteAssistedVolumeSnapshot.yaml

	- delete_info: delete_info






Response
^^^^^^^^



