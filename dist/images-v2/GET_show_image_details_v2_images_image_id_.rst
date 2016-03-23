=============================================================================
Show Image Details -  OpenStack Image API v2
=============================================================================

Show Image Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_image_details_v2_images_image_id_.rst#request>`__
`Response <GET_show_image_details_v2_images_image_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/images/{image_id}

(Since Image API v2.0) Shows details for an image.

The response body contains a single image entity.

Preconditions

The image must exist.



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





**Example Show Image Details: JSON request**


.. code::

    {
        "status": "active",
        "name": "cirros-0.3.2-x86_64-disk",
        "tags": [],
        "container_format": "bare",
        "created_at": "2014-05-05T17:15:10Z",
        "disk_format": "qcow2",
        "updated_at": "2014-05-05T17:15:11Z",
        "visibility": "public",
        "self": "/v2/images/1bea47ed-f6a9-463b-b423-14b9cca9ad27",
        "min_disk": 0,
        "protected": false,
        "id": "1bea47ed-f6a9-463b-b423-14b9cca9ad27",
        "file": "/v2/images/1bea47ed-f6a9-463b-b423-14b9cca9ad27/file",
        "checksum": "64d7c1cd2b6f60c92c14662941cb7913",
        "owner": "5ef70662f8b34079a6eddb8da9d75fe8",
        "size": 13167616,
        "min_ram": 0,
        "schema": "/v2/schemas/image",
        "virtual_size": null
    }
    

