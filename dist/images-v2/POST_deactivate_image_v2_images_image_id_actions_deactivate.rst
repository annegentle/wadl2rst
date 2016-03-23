=============================================================================
Deactivate Image -  OpenStack Image API v2
=============================================================================

Deactivate Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_deactivate_image_v2_images_image_id_actions_deactivate.rst#request>`__
`Response <POST_deactivate_image_v2_images_image_id_actions_deactivate.rst#response>`__

.. code-block:: javascript

    POST /v2/images/{image_id}/actions/deactivate

(Since Image API v2.0) Deactivates an image.

If you try to download a deactivated image, the call returns the ``Forbidden (403)`` response code. Also, only administrative users can view image locations for deactivated images.

The deactivate operation returns an error if the image status is not ``active`` or ``deactivated``.

Preconditions

The image must exist.



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




