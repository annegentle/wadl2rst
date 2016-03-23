=============================================================================
Add Image Tag -  OpenStack Image API v2
=============================================================================

Add Image Tag
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_add_image_tag_v2_images_image_id_tags_tag_.rst#request>`__
`Response <PUT_add_image_tag_v2_images_image_id_tags_tag_.rst#response>`__

.. code-block:: javascript

    PUT /v2/images/{image_id}/tags/{tag}

(Since Image API v2.0) Adds a tag to an image.



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




