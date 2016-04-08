
Show Image Details
==================

`Request <GET_show_image_details_v2_tenant_id_images_image_id_.rst#request>`__
`Response <GET_show_image_details_v2_tenant_id_images_image_id_.rst#response>`__

.. rest_method:: GET /v2/{tenant_id}/images/{image_id}

Shows details for an image.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: showImageDetails.yaml

	- os-disk-config:diskConfig: os-disk-config:diskConfig




**Example Show Image Details: JSON request**


.. code::

    

