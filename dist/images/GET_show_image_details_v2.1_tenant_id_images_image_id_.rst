
Show Image Details
==================

`Request <GET_show_image_details_v2.1_tenant_id_images_image_id_.rst#request>`__
`Response <GET_show_image_details_v2.1_tenant_id_images_image_id_.rst#response>`__

.. rest_method:: GET //v2.1/{tenant_id}/images/{image_id}

Shows details for an image.



Normal response codes: 200,203,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Image Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/images/image-show-resp.json
   :language: javascript

