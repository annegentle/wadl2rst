
Create Or Update Image Metadata Item
====================================

.. rest_method:: PUT //v2.1/{tenant_id}/images/{image_id}/metadata/{key}

Creates or updates a metadata item, by key, for an image.



Normal response codes: 200,,503,400,401,403,405,404,415,400,409

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../createOrUpdateImageMetadataItem.yaml

	- tenant_id: tenant_id
	- image_id: image_id
	- key: key








**Example Create Or Update Image Metadata Item: JSON request**


.. literalinclude:: ../../../doc/api_samples/images/image-metadata-item-update-req.json
   :language: javascript



Response
^^^^^^^^





**Example Create Or Update Image Metadata Item: JSON request**


.. literalinclude:: ../../../doc/api_samples/images/image-metadata-item-update-resp.json
   :language: javascript


