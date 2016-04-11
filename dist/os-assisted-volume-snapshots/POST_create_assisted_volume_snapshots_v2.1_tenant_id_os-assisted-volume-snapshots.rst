
Create Assisted Volume Snapshots
================================

`Request <POST_create_assisted_volume_snapshots_v2.1_tenant_id_os-assisted-volume-snapshots.rst#request>`__
`Response <POST_create_assisted_volume_snapshots_v2.1_tenant_id_os-assisted-volume-snapshots.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-assisted-volume-snapshots

Creates an assisted volume snapshot.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: ../createAssistedVolumeSnapshots.yaml

	- snapshot: snapshot
	- volume_id: volume_id
	- create_info: create_info
	- snapshot_id: snapshot_id
	- type: type
	- new_file: new_file




**Example Create Assisted Volume Snapshots: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-assisted-volume-snapshots/snapshot-create-assisted-req.json
   :language: javascript



Response
^^^^^^^^


.. rest_parameters:: ../createAssistedVolumeSnapshots.yaml

	- id: id
	- volume_id: volume_id




**Example Create Assisted Volume Snapshots: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-assisted-volume-snapshots/snapshot-create-assisted-resp.json
   :language: javascript

