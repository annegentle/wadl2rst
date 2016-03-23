=============================================================================
Add Members To Image -  OpenStack Image API v1
=============================================================================

Add Members To Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_add_members_to_image_v1_images_image_id_members_owner_id_.rst#request>`__
`Response <PUT_add_members_to_image_v1_images_image_id_members_owner_id_.rst#response>`__

.. code-block:: javascript

    PUT /v1/images/{image_id}/members/{owner_id}

Adds one or more members to an image.

If you omit the request body, this call adds the membership to the image, leaves the existing memberships unmodified, and sets the ``can_share`` attribute to ``false`` for new memberships.



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
|can_share                 |xsd:boolean *(Required)* |Indicates whether the    |
|                          |                         |owner is authorized to   |
|                          |                         |share the image. If the  |
|                          |                         |owner can share the      |
|                          |                         |image, this value is     |
|                          |                         |``true``. Otherwise,     |
|                          |                         |this value is ``false``. |
|                          |                         |Specify the owner ID,    |
|                          |                         |which is the tenant ID,  |
|                          |                         |is in the request URI.   |
+--------------------------+-------------------------+-------------------------+





**Example Add Members To Image: JSON request**


.. code::

    {
        "members": [
            {
                "member_id": "tenant1",
                "can_share": false
            },
            {
                "member_id": "tenant2",
                "can_share": false
            }
        ]
    }
    


Response
^^^^^^^^^^^^^^^^^^




