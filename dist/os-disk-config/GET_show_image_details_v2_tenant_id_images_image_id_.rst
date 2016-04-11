
Show Image Details
==================

.. rest_method:: GET /v2/{tenant_id}/images/{image_id}

Shows details for an image.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showImageDetails.yaml

	- tenant_id: tenant_id
	- image_id: image_id








Response
^^^^^^^^


.. rest_parameters:: ../showImageDetails.yaml

	- os-disk-config:diskConfig: os-disk-config:diskConfig




**Example Show Image Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-disk-config/image-get-resp.json
   :language: javascript


