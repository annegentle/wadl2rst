
Create Volume
=============

.. rest_method:: POST /v2.1/{tenant_id}/os-volumes

Creates a volume.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createVolume.yaml

	- tenant_id: tenant_id





Body Parameters
~~~~~~~~~~~~~~~

.. rest_parameters:: ../createVolume.yaml

	- volume: volume
	- display_name: display_name
	- display_description: display_description
	- size: size
	- volume_type: volume_type
	- metadata: metadata
	- availability_zone: availability_zone
	- snapshot_id: snapshot_id




**Example Create Volume: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/volume-create-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Volume: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/volume-show-resp.json
   :language: javascript


