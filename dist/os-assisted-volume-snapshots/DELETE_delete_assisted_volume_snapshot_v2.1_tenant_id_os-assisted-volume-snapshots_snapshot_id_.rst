
Delete Assisted Volume Snapshot
===============================

.. rest_method:: DELETE /v2.1/{tenant_id}/os-assisted-volume-snapshots/{snapshot_id}

Deletes an assisted volume snapshot.

To make this request, add the ``delete_info`` query parameter to the URI, as follows:

DELETE /os-assisted-volume-snapshots?delete_info='{"volume_id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c"}'

Normal response codes: 204

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteAssistedVolumeSnapshot.yaml

	- tenant_id: tenant_id
	- snapshot_id: snapshot_id



Query Parameters
~~~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteAssistedVolumeSnapshot.yaml

	- delete_info: delete_info






Response
^^^^^^^^




