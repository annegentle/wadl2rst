=============================================================================
Delete Image Tag -  OpenStack Image API v2
=============================================================================

Delete Image Tag
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_image_tag_v2_images_image_id_tags_tag_.rst#request>`__
`Response <DELETE_delete_image_tag_v2_images_image_id_tags_tag_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/images/{image_id}/tags/{tag}

(Since Image API v2.0) Deletes a tag from an image.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{image_id}                |csapi:UUID               |The UUID of the image.   |
+--------------------------+-------------------------+-------------------------+
|{tag}                     |xsd:string               |The image tag.           |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




