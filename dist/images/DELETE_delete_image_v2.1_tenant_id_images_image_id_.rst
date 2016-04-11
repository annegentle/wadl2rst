
Delete Image
============

.. rest_method:: DELETE //v2.1/{tenant_id}/images/{image_id}

Deletes an image.



Normal response codes: 204,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../deleteImage.yaml

	- tenant_id: tenant_id
	- image_id: image_id








Response
^^^^^^^^




