=============================================================================
Delete Image -  OpenStack Image API v2
=============================================================================

Delete Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_image_v2_images_image_id_.rst#request>`__
`Response <DELETE_delete_image_v2_images_image_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/images/{image_id}

(Since Image API v2.0) Deletes an image.

You cannot delete images with the ``protected`` attribute set to ``true`` (boolean).

Preconditions

You can delete an image in any status except ``deleted``.

First, set the ``protected`` attribute to ``false`` (boolean). Then, perform the delete.

Synchronous Postconditions

The response is empty and returns the HTTP ``204`` response code.

The API deletes the image from the images index.

If the image stores binary image data in the storage node, the OpenStack Image service deletes the data from the node.

Troubleshooting

The call returns the HTTP ``403`` response code when the ``protected`` attribute is set to ``true`` even if you have correct permissions. Ensure that you meet the preconditions and run the request again. If the request fails again, review your API request.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
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








Response
^^^^^^^^^^^^^^^^^^




