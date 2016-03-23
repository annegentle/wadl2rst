=============================================================================
Delete Image Member -  OpenStack Image API v2
=============================================================================

Delete Image Member
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_image_member_v2_images_image_id_members_member_id_.rst#request>`__
`Response <DELETE_delete_image_member_v2_images_image_id_members_member_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/images/{image_id}/members/{member_id}

(Since Image API v2.1) Deletes a tenant ID from the member list of an image.

Preconditions

The image must exist.

You must be the owner of the image.

Synchronous Postconditions

The API removes the member from the image members.

Troubleshooting

Even if you have correct permissions, if you are not the owner of the image or you specify an incorrect image ID or member ID, the call returns the HTTP ``403`` or ``404`` response code. Ensure that you meet the preconditions and run the request again. If the request fails again, review your API request URI.



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
|{member_id}               |xsd:string               |The ID of the image      |
|                          |                         |member. An image member  |
|                          |                         |is a tenant with whom    |
|                          |                         |the image is shared.     |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




