=============================================================================
Update Image -  OpenStack Image API v1
=============================================================================

Update Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_image_v1_images_image_id_.rst#request>`__
`Response <PUT_update_image_v1_images_image_id_.rst#response>`__

.. code-block:: javascript

    PUT /v1/images/{image_id}

Updates an image, uploads an image file, or updates metadata for an image.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{image_id}                |xsd:string               |Image ID stored through  |
|                          |                         |the image API. Typically |
|                          |                         |a UUID.                  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|location                  |xsd:anyURI *(Required)*  |` <None>`__              |
+--------------------------+-------------------------+-------------------------+




