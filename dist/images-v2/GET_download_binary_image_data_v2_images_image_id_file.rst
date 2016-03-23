=============================================================================
Download Binary Image Data -  OpenStack Image API v2
=============================================================================

Download Binary Image Data
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_download_binary_image_data_v2_images_image_id_file.rst#request>`__
`Response <GET_download_binary_image_data_v2_images_image_id_file.rst#response>`__

.. code-block:: javascript

    GET /v2/images/{image_id}/file

(Since Image API v2.0) Downloads binary image data.

Example call: ``curl -i -X GET -H "X-Auth-Token: $token" $image_url/v2/images/{image_id}/file``

The response body contains the raw binary data that represents the actual virtual disk. The ``Content-Type`` header contains the ``application/octet-stream`` value. The ``Content-MD5`` header contains an MD5 checksum of the image data. Use this checksum to verify the integrity of the image data.



Preconditions

The images must exist.

Synchronous Postconditions

You can download the binary image data in your machine if the image has image data.

If image data exists, the call returns the HTTP ``200`` response code.

If no image data exists, the call returns the HTTP ``204`` response code.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
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




