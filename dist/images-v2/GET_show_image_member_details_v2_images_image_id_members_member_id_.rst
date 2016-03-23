=============================================================================
Show Image Member Details -  OpenStack Image API v2
=============================================================================

Show Image Member Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_image_member_details_v2_images_image_id_members_member_id_.rst#request>`__
`Response <GET_show_image_member_details_v2_images_image_id_members_member_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/images/{image_id}/members/{member_id}

(Since Image API v2.2) Shows image member details.

Response body is a single image member entity.

Preconditions

The image must exist.

You must be the owner or a member of the image.



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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|status          |xsd:string     |The image status.                            |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|created_at      |xsd:dateTime   |The date and time when the resource was      |
|                |*(Required)*   |created. The date and time stamp format is   |
|                |               |`ISO 8601                                    |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                |               |``2015-08-27T09:49:58-05:00``. The           |
|                |               |``±hh:mm`` value, if included, is the time   |
|                |               |zone as an offset from UTC.                  |
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
|image_id        |csapi:UUID     |The UUID of the image.                       |
|                |*(Required)*   |                                             |
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





**Example Show Image Member Details: JSON request**


.. code::

    {
        "status": "pending",
        "created_at": "2013-11-26T07:21:21Z",
        "updated_at": "2013-11-26T07:21:21Z",
        "image_id": "0ae74cc5-5147-4239-9ce2-b0c580f7067e",
        "member_id": "8989447062e04a818baf9e073fd04fa7",
        "schema": "/v2/schemas/member"
    }
    

