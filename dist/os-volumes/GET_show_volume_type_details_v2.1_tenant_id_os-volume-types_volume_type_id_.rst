
Show Volume Type Details
========================

.. rest_method:: GET /v2.1/{tenant_id}/os-volume-types/{volume_type_id}

Shows details for a volume type.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showVolumeTypeDetails.yaml

	- tenant_id: tenant_id
	- volume_type_id: volume_type_id








Response
^^^^^^^^





**Example Show Volume Type Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/volume-type-show-resp.json
   :language: javascript


