=============================================================================
Create Image Member -  OpenStack Image API v2
=============================================================================

Create Image Member
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_image_member_v2_images_image_id_members.rst#request>`__
`Response <POST_create_image_member_v2_images_image_id_members.rst#response>`__

.. code-block:: javascript

    POST /v2/images/{image_id}/members

(Since Image API v2.1) Adds a tenant ID as an image member.

This call accepts either the ``member_id`` or ``member`` attribute in the request body. If you specify both attributes, the API uses the ``member_id`` value and ignores the ``member`` value. Use of the ``member`` attribute is supported but deprecated. Use of the ``member_id`` attribute is preferred.

Preconditions

The images must exist.

You can add a member to a private image.

You must be the owner of the image.

Synchronous Postconditions

With correct permissions, you can see the member status of the image as ``pending`` through API calls.

Troubleshooting

Even if you have correct permissions, if the ``visibility`` attribute is set to ``public``, the request returns the HTTP ``403`` response code. Ensure that you meet the preconditions and run the request again. If the request fails again, review your API request.

If the member is already a member for the image, the service returns the ``Conflict (409)`` response code. If you meant to specify a different member, run the request again.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{image_id}                |csapi:UUID               |The UUID of the image.   |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|member_id                 |xsd:string *(Required)*  |The ID of the image      |
|                          |                         |member. An image member  |
|                          |                         |is a tenant with whom    |
|                          |                         |the image is shared.     |
|                          |                         |This call accepts either |
|                          |                         |the ``member_id`` or     |
|                          |                         |``member`` attribute in  |
|                          |                         |the request body. If you |
|                          |                         |specify both attributes, |
|                          |                         |the API uses the         |
|                          |                         |``member_id`` value and  |
|                          |                         |ignores the ``member``   |
|                          |                         |value. Use of the        |
|                          |                         |``member`` attribute is  |
|                          |                         |supported but            |
|                          |                         |deprecated. Use of the   |
|                          |                         |``member_id`` attribute  |
|                          |                         |is preferred.            |
+--------------------------+-------------------------+-------------------------+
|member                    |xsd:string *(Required)*  |The ID of the image      |
|                          |                         |member. An image member  |
|                          |                         |is a tenant with whom    |
|                          |                         |the image is shared.     |
|                          |                         |This call accepts either |
|                          |                         |the ``member_id`` or     |
|                          |                         |``member`` attribute in  |
|                          |                         |the request body. If you |
|                          |                         |specify both attributes, |
|                          |                         |the API uses the         |
|                          |                         |``member_id`` value and  |
|                          |                         |ignores the ``member``   |
|                          |                         |value. Use of the        |
|                          |                         |``member`` attribute is  |
|                          |                         |supported but            |
|                          |                         |deprecated. Use of the   |
|                          |                         |``member_id`` attribute  |
|                          |                         |is preferred.            |
+--------------------------+-------------------------+-------------------------+





**Example Create Image Member: JSON request**


.. code::

    {
        "member": "8989447062e04a818baf9e073fd04fa7"
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





**Example Create Image Member: JSON request**


.. code::

    {
        "created_at": "2013-09-20T19:22:19Z",
        "image_id": "a96be11e-8536-4910-92cb-de50aa19dfe6",
        "member_id": "8989447062e04a818baf9e073fd04fa7",
        "schema": "/v2/schemas/member",
        "status": "pending",
        "updated_at": "2013-09-20T19:25:31Z"
    }
    

