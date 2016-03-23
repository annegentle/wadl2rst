=============================================================================
Update Image -  OpenStack Image API v2
=============================================================================

Update Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PATCH_update_image_v2_images_image_id_.rst#request>`__
`Response <PATCH_update_image_v2_images_image_id_.rst#response>`__

.. code-block:: javascript

    PATCH /v2/images/{image_id}

(Since Image API v2.0) Updates an image.

Depending on the referenced target location, this operation performs one of these actions:

Image update actionsTarget locationUpdate actionAn array index

The API inserts a new value into the array at the index.

An object member that does not exist

The API adds a member to the object.

An object member that exists

The member value is replaced.

The operation object must contain a ``value`` member that contains the value to add. For example:

{"op": "add","path": "/a/b/c","value": ["foo","bar"]}The target location must reference one of these values:

The root of the target document. The value is the entire content of the target document.

A member value to add to an object. The API adds the value to the object at the location. If the member already exists, the API replaces it with the value.

An element to add to the array. The API adds the element value to the array at the location. The API shifts any element that is at or above the index one position to the right. The index must not be greater than the number of elements in the array. If you use the hyphen (-) character to index the end of the array, the API appends the value to the array. See `JavaScriptObject Notation (JSON) Pointer <http://tools.ietf.org/html/rfc6901>`__.

Because this operation adds to existing objects and arrays, its target location often does not exist.

The request body must conform to one of these media types:

``application/openstack-images-v2.0-json-patch``

``application/openstack-images-v2.1-json-patch`` (since Image API v2.2)

You can also use the ``PATCH`` method to add or remove image properties.

For information about the ``PATCH`` method and the available media types, see `Image API v2 HTTP PATCH media types <http://specs.openstack.org/openstack/glance-specs/specs/api/v2/http-patch-image-api-v2.html>`__.

Preconditions

When you add a location to or replace a location in the image, you must set the ``disk_format`` and ``container_format`` parameters in the image.

When you replace a location, that location must be previously set in the image.

Synchronous Postconditions

With correct permissions, you can view the updated values of the attributes of the image.

After you add a location to an image that had no location and with correct permissions, you can use API calls to view the image status as ``active``.

After you remove all locations from the image and with correct permissions, you can use API calls to view the image status as ``queued``.

Troubleshooting

If you cannot update locations, your request might be missing some information. Make sure that you meet the preconditions and run the request again. If the request fails again, review your API request.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|path                      |xsd:string *(Required)*  |An image property.       |
+--------------------------+-------------------------+-------------------------+
|value                     |xsd:string *(Required)*  |Value of image property  |
|                          |                         |used in add or replace   |
|                          |                         |operations expressed in  |
|                          |                         |JSON notation. For       |
|                          |                         |example, you must        |
|                          |                         |enclose strings in       |
|                          |                         |quotation marks, and you |
|                          |                         |do not enclose numeric   |
|                          |                         |values in quotation      |
|                          |                         |marks.                   |
+--------------------------+-------------------------+-------------------------+
|op                        |xsd:string *(Required)*  |The operation. A valid   |
|                          |                         |value is: ``add``. Adds  |
|                          |                         |a property or location   |
|                          |                         |in the image.            |
|                          |                         |``remove``. Removes an   |
|                          |                         |image's property or      |
|                          |                         |location. ``replace``.   |
|                          |                         |Replaces the value of an |
|                          |                         |image's property or      |
|                          |                         |location.                |
+--------------------------+-------------------------+-------------------------+
|url                       |xsd:string *(Required)*  |The URL to access the    |
|                          |                         |image file kept in       |
|                          |                         |external store.          |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:dict *(Required)*    |The location metadata.   |
+--------------------------+-------------------------+-------------------------+





**Example Update Image: JSON request**


.. code::

    [
        {
            "op": "replace",
            "path": "/name",
            "value": "Fedora 17"
        },
        {
            "op": "replace",
            "path": "/tags",
            "value": [
                "fedora",
                "beefy"
            ]
        }
    ]
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+-----------------+--------------+---------------------------------------------+
|Name             |Type          |Description                                  |
+=================+==============+=============================================+
|status           |xsd:string    |The image status.                            |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|name             |xsd:string    |The name of the image. Value might be        |
|                 |*(Required)*  |``null`` (JSON null data type).              |
+-----------------+--------------+---------------------------------------------+
|tags             |xsd:list      |A list of ``tag`` objects.                   |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|container_format |xsd:string    |The container format of the image. The value |
|                 |*(Required)*  |might be ``null`` (JSON null data type).     |
+-----------------+--------------+---------------------------------------------+
|created_at       |xsd:dateTime  |The date and time when the resource was      |
|                 |*(Required)*  |created. The date and time stamp format is   |
|                 |              |`ISO 8601                                    |
|                 |              |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                 |              |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                 |              |``2015-08-27T09:49:58-05:00``. The           |
|                 |              |``±hh:mm`` value, if included, is the time   |
|                 |              |zone as an offset from UTC.                  |
+-----------------+--------------+---------------------------------------------+
|disk_format      |xsd:string    |The disk format of the image. The value      |
|                 |*(Required)*  |might be ``null`` (JSON null data type).     |
+-----------------+--------------+---------------------------------------------+
|updated_at       |xsd:dateTime  |The date and time when the resource was      |
|                 |*(Required)*  |updated. The date and time stamp format is   |
|                 |              |`ISO 8601                                    |
|                 |              |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                 |              |: CCYY-MM-DDThh:mm:ss±hh:mmFor example,      |
|                 |              |``2015-08-27T09:49:58-05:00``. The           |
|                 |              |``±hh:mm`` value, if included, is the time   |
|                 |              |zone as an offset from UTC. In the previous  |
|                 |              |example, the offset value is ``-05:00``. If  |
|                 |              |the ``updated_at`` date and time stamp is    |
|                 |              |not set, its value is ``null``.              |
+-----------------+--------------+---------------------------------------------+
|min_disk         |xsd:int       |The minimum disk size in GB that is required |
|                 |*(Required)*  |to boot the image. The value might be        |
|                 |              |``null`` (JSON null data type).              |
+-----------------+--------------+---------------------------------------------+
|protected        |xsd:boolean   |Image protection for deletion. A valid value |
|                 |*(Required)*  |is ``True`` or ``False``. Default is         |
|                 |              |``False``.                                   |
+-----------------+--------------+---------------------------------------------+
|id               |csapi:UUID    |The UUID of the image.                       |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|min_ram          |xsd:int       |The minimum amount of RAM in MB that is      |
|                 |*(Required)*  |required to boot the image. The value might  |
|                 |              |be ``null`` (JSON null data type).           |
+-----------------+--------------+---------------------------------------------+
|checksum         |xsd:string    |Hash that is used over the the image data.   |
|                 |*(Required)*  |The Image service uses this value for        |
|                 |              |verification. The value might be ``null``    |
|                 |              |(JSON null data type).                       |
+-----------------+--------------+---------------------------------------------+
|owner            |csapi:UUID    |The ID of the owner, or tenant, of the       |
|                 |*(Required)*  |image. The value might be ``null`` (JSON     |
|                 |              |null data type).                             |
+-----------------+--------------+---------------------------------------------+
|visibility       |xsd:string    |The image visibility. A valid value is       |
|                 |*(Required)*  |``public`` or ``private``. Default is        |
|                 |              |``private``.                                 |
+-----------------+--------------+---------------------------------------------+
|size             |xsd:int       |The size of the image data, in bytes. The    |
|                 |*(Required)*  |value might be ``null`` (JSON null data      |
|                 |              |type).                                       |
+-----------------+--------------+---------------------------------------------+
|locations        |xsd:list      |A list of URLs to access the image file in   |
|                 |*(Required)*  |external store. This list appears if the     |
|                 |              |``show_multiple_locations`` option is set to |
|                 |              |``True`` in the Image service's              |
|                 |              |configuration file.                          |
+-----------------+--------------+---------------------------------------------+
|metadata         |xsd:dict      |The location metadata.                       |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|properties       |xsd:dict      |The image properties, if any.                |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|direct_url       |xsd:string    |The URL to access the image file kept in     |
|                 |*(Required)*  |external store. It appears when you set the  |
|                 |              |``show_image_direct_url`` option to ``True`` |
|                 |              |in the Image service's configuration file.   |
+-----------------+--------------+---------------------------------------------+
|self             |xsd:string    |The URL for the virtual machine image.       |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|file             |xsd:string    |The URL for the virtual machine image file.  |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|schema           |xsd:string    |The URL for schema of the virtual machine    |
|                 |*(Required)*  |image.                                       |
+-----------------+--------------+---------------------------------------------+





**Example Update Image: JSON request**


.. code::

    {
        "id": "da3b75d9-3f4a-40e7-8a2c-bfab23927dea",
        "name": "Fedora 17",
        "status": "active",
        "visibility": "public",
        "size": 2254249,
        "checksum": "2cec138d7dae2aa59038ef8c9aec2390",
        "tags": [
            "fedora",
            "beefy"
        ],
        "created_at": "2012-08-10T19:23:50Z",
        "updated_at": "2012-08-12T11:11:33Z",
        "self": "/v2/images/da3b75d9-3f4a-40e7-8a2c-bfab23927dea",
        "file": "/v2/images/da3b75d9-3f4a-40e7-8a2c-bfab23927dea/file",
        "schema": "/v2/schemas/image",
        "owner": null,
        "min_ram": null,
        "min_disk": null,
        "disk_format": null,
        "virtual_size": null,
        "container_format": null
    }
    

