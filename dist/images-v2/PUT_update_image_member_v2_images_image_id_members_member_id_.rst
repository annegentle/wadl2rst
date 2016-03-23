=============================================================================
Update Image Member -  OpenStack Image API v2
=============================================================================

Update Image Member
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_image_member_v2_images_image_id_members_member_id_.rst#request>`__
`Response <PUT_update_image_member_v2_images_image_id_members_member_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2/images/{image_id}/members/{member_id}

(Since Image API v2.1) Sets the status for an image member.

Preconditions

The images must exist.

You must be a member of the image.

Synchronous Postconditions

If you update the member status to ``accepted`` and have the correct permissions, you see the image in list images responses.

With correct permissions, you can make API calls to see the updated member status of the image.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|status                    |xsd:string *(Required)*  |The status of this image |
|                          |                         |member.                  |
+--------------------------+-------------------------+-------------------------+





**Example Update Image Member: JSON request**


.. code::

    {
        "status": "accepted"
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|created_at      |xsd:dateTime   |The date and time when the resource was      |
|                |*(Required)*   |created. The date and time stamp format is   |
|                |               |`ISO 8601                                    |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                |               |``2015-08-27T09:49:58-05:00``. The           |
|                |               |``±hh:mm`` value, if included, is the time   |
|                |               |zone as an offset from UTC.                  |
+----------------+---------------+---------------------------------------------+
|member_id       |xsd:string     |The ID of the image member. An image member  |
|                |*(Required)*   |is a tenant with whom the image is shared.   |
|                |               |This call accepts either the ``member_id``   |
|                |               |or ``member`` attribute in the request body. |
|                |               |If you specify both attributes, the API uses |
|                |               |the ``member_id`` value and ignores the      |
|                |               |``member`` value. Use of the ``member``      |
|                |               |attribute is supported but deprecated. Use   |
|                |               |of the ``member_id`` attribute is preferred. |
+----------------+---------------+---------------------------------------------+
|schema          |xsd:string     |The URL for schema of the member.            |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|status          |xsd:string     |The image status.                            |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|updated_at      |xsd:dateTime   |The date and time when the resource was      |
|                |*(Required)*   |updated. The date and time stamp format is   |
|                |               |`ISO 8601                                    |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                |               |``2015-08-27T09:49:58-05:00``. The           |
|                |               |``±hh:mm`` value, if included, is the time   |
|                |               |zone as an offset from UTC. In the previous  |
|                |               |example, the offset value is ``-05:00``. If  |
|                |               |the ``updated_at`` date and time stamp is    |
|                |               |not set, its value is ``null``.              |
+----------------+---------------+---------------------------------------------+





**Example Update Image Member: JSON request**


.. code::

    {
        "created_at": "2013-09-20T19:22:19Z",
        "image_id": "a96be11e-8536-4910-92cb-de50aa19dfe6",
        "member_id": "8989447062e04a818baf9e073fd04fa7",
        "schema": "/v2/schemas/member",
        "status": "accepted",
        "updated_at": "2013-09-20T20:15:31Z"
    }
    

