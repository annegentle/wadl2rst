=============================================================================
Replace Member -  OpenStack Image API v1
=============================================================================

Replace Member
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_replace_member_v1_images_image_id_members.rst#request>`__
`Response <PUT_replace_member_v1_images_image_id_members.rst#response>`__

.. code-block:: javascript

    PUT /v1/images/{image_id}/members

Replaces a membership list for an image.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|memberships               |*(Required)*             |                         |
+--------------------------+-------------------------+-------------------------+
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





**Example Replace Member: JSON request**


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




