=============================================================================
Show Image Metadata -  OpenStack Image API v1
=============================================================================

Show Image Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <HEAD_show_image_metadata_v1_images_image_id_.rst#request>`__
`Response <HEAD_show_image_metadata_v1_images_image_id_.rst#response>`__

.. code-block:: javascript

    HEAD /v1/images/{image_id}

Shows the image metadata information in the body of the response.

The Image system does not return a response body for the ``HEAD`` operation.

Example requests and responses:

Show image metadata:

http://glance.example.com/v1/images/03bc0a8b-659c-4de9-b6bd-13c6e86e6455



X-Image-Meta-Checksum → 8a40c862b5735975d82605c1dd395796X-Image-Meta-Container_format → akiX-Image-Meta-Created_at → 2016-01-06T03:22:20.000000X-Image-Meta-Deleted → FalseX-Image-Meta-Disk_format → akiX-Image-Meta-Id → 03bc0a8b-659c-4de9-b6bd-13c6e86e6455X-Image-Meta-Is_public → TrueX-Image-Meta-Min_disk → 0X-Image-Meta-Min_ram → 0X-Image-Meta-Name → cirros-0.3.4-x86_64-uec-kernelX-Image-Meta-Owner → 13cc6052265b41529e2fd0fc461fa8efX-Image-Meta-Protected → FalseX-Image-Meta-Size → 4979632X-Image-Meta-Status → deactivatedX-Image-Meta-Updated_at → 2016-02-25T03:02:05.000000X-Openstack-Request-Id → req-d5208320-28ed-4c22-b628-12dc6456d983

If the request succeeds, the operation returns the ``200`` response code.

If there is an image size mismatch detected with the ``X-Image-Meta-Size``, the operation returns a ``409`` response code.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
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




