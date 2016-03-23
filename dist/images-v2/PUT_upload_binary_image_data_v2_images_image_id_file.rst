=============================================================================
Upload Binary Image Data -  OpenStack Image API v2
=============================================================================

Upload Binary Image Data
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_upload_binary_image_data_v2_images_image_id_file.rst#request>`__
`Response <PUT_upload_binary_image_data_v2_images_image_id_file.rst#response>`__

.. code-block:: javascript

    PUT /v2/images/{image_id}/file

(Since Image API v2.0) Uploads binary image data.

Set the ``Content-Type`` request header to ``application/octet-stream``.

Example call:

curl -i -X PUT -H "X-Auth-Token: $token" -H "Content-Type: application/octet-stream" \-d @/home/glance/ubuntu-12.10.qcow2 $image_url/v2/images/{image_id}/filePreconditions

Before you can store binary image data, you must meet the following preconditions:

The image must exist.

You must set the disk and container formats in the image.

The image status must be ``queued``.

Your image storage quota must be sufficient.

The size of the data that you want to store must not exceed the size that the OpenStack Image service allows.

Synchronous Postconditions

With correct permissions, you can see the image status as ``active`` through API calls.

With correct access, you can see the stored data in the storage system that OpenStack Image service manages.

Troubleshooting

If you cannot store the data, either your request lacks required information or you exceeded your allotted quota. Ensure that you meet the preconditions and run the request again. If the request fails again, review your API request.

The storage back ends for storing the data must have enough free storage space to accommodate the size of the data.



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
|{image_id}                |csapi:UUID               |The UUID of the image.   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




