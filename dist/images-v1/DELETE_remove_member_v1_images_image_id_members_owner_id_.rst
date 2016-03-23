=============================================================================
Remove Member -  OpenStack Image API v1
=============================================================================

Remove Member
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_remove_member_v1_images_image_id_members_owner_id_.rst#request>`__
`Response <DELETE_remove_member_v1_images_image_id_members_owner_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v1/images/{image_id}/members/{owner_id}

Removes a member from an image.



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
|{owner_id}                |xsd:string               |Owner ID, which is the   |
|                          |                         |tenant ID.               |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|member_id                 |csapi:UUID *(Required)*  |The UUID of the member   |
|                          |                         |with which an image is   |
|                          |                         |shared.                  |
+--------------------------+-------------------------+-------------------------+





Response
^^^^^^^^^^^^^^^^^^




