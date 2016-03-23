=============================================================================
Delete Image -  OpenStack Image API v1
=============================================================================

Delete Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_image_v1_images_image_id_.rst#request>`__
`Response <DELETE_delete_image_v1_images_image_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v1/images/{image_id}

Deletes an image.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
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




