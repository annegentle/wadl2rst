=============================================================================
Reactivate Image -  OpenStack Image API v2
=============================================================================

Reactivate Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_reactivate_image_v2_images_image_id_actions_reactivate.rst#request>`__
`Response <POST_reactivate_image_v2_images_image_id_actions_reactivate.rst#response>`__

.. code-block:: javascript

    POST /v2/images/{image_id}/actions/reactivate

(Since Image API v2.0) Reactivates an image.

The reactivate operation returns an error if the image status is not ``active`` or ``deactivated``.

Preconditions

The image must exist.



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








Response
^^^^^^^^^^^^^^^^^^




