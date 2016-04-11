
Delete Volume
=============

.. rest_method:: DELETE /v2.1/{tenant_id}/os-volumes/{volume_id}

Deletes a volume.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteVolume.yaml

	- tenant_id: tenant_id
	- volume_id: volume_id








Response
^^^^^^^^





**Example Delete Volume: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/volume-delete-json-http.txt
   :language: javascript


