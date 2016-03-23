=============================================================================
Create Image -  OpenStack Image API v2
=============================================================================

Create Image
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_image_v2_images.rst#request>`__
`Response <POST_create_image_v2_images.rst#response>`__

.. code-block:: javascript

    POST /v2/images

(Since Image API v2.0) Creates a virtual machine (VM) image.

The ``Location`` response header contains the URI for the image. The response body contains the new image entity.

Synchronous Postconditions

With correct permissions, you can see the image status as ``queued`` through API calls.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |Name for the image. Note |
|                          |                         |that the name of an      |
|                          |                         |image is not unique to   |
|                          |                         |an Image service node.   |
|                          |                         |The API cannot expect    |
|                          |                         |users to know the names  |
|                          |                         |of images that other     |
|                          |                         |users own.               |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |A unique, user-defined   |
|                          |                         |image UUID, in the       |
|                          |                         |format: nnnnnnnn-nnnn-   |
|                          |                         |nnnn-nnnn-               |
|                          |                         |nnnnnnnnnnnnWhere n is a |
|                          |                         |hexadecimal digit from 0 |
|                          |                         |to f, or F. For example: |
|                          |                         |b2173dd3-7ad6-4362-baa6- |
|                          |                         |a68bce3565cbIf you omit  |
|                          |                         |this value, the API      |
|                          |                         |generates a UUID for the |
|                          |                         |image.                   |
+--------------------------+-------------------------+-------------------------+
|visibility                |xsd:string *(Required)*  |Image visibility. Valid  |
|                          |                         |value is ``public`` or   |
|                          |                         |``private``. Default is  |
|                          |                         |``public``.              |
+--------------------------+-------------------------+-------------------------+
|tags                      |xsd:list *(Required)*    |Image tags.              |
+--------------------------+-------------------------+-------------------------+
|container_format          |xsd:string *(Required)*  |Format of the container. |
|                          |                         |A valid value is         |
|                          |                         |``ami``, ``ari``,        |
|                          |                         |``aki``, ``bare``,       |
|                          |                         |``ovf``, ``ova``, or     |
|                          |                         |``docker``.              |
+--------------------------+-------------------------+-------------------------+
|disk_format               |xsd:string *(Required)*  |The format of the disk.  |
|                          |                         |A valid value is         |
|                          |                         |``ami``, ``ari``,        |
|                          |                         |``aki``, ``vhd``,        |
|                          |                         |``vmdk``, ``raw``,       |
|                          |                         |``qcow2``, ``vdi``, or   |
|                          |                         |``iso``.                 |
+--------------------------+-------------------------+-------------------------+
|min_disk                  |xsd:int *(Required)*     |Amount of disk space in  |
|                          |                         |GB that is required to   |
|                          |                         |boot the image.          |
+--------------------------+-------------------------+-------------------------+
|min_ram                   |xsd:int *(Required)*     |Amount of RAM in MB that |
|                          |                         |is required to boot the  |
|                          |                         |image.                   |
+--------------------------+-------------------------+-------------------------+
|protected                 |xsd:boolean *(Required)* |Image protection for     |
|                          |                         |deletion. Valid value is |
|                          |                         |``true`` or ``false``.   |
|                          |                         |Default is ``false``.    |
+--------------------------+-------------------------+-------------------------+
|properties                |xsd:dict *(Required)*    |The image properties, if |
|                          |                         |any.                     |
+--------------------------+-------------------------+-------------------------+





**Example Create Image: JSON request**


.. code::

    {
        "container_format": "bare",
        "disk_format": "raw",
        "name": "Ubuntu",
        "id": "b2173dd3-7ad6-4362-baa6-a68bce3565cb"
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+-----------------+--------------+---------------------------------------------+
|Name             |Type          |Description                                  |
+=================+==============+=============================================+
|status           |xsd:string    |The image status.                            |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|container_format |xsd:string    |The container format of the image. The value |
|                 |*(Required)*  |might be ``null`` (JSON null data type).     |
+-----------------+--------------+---------------------------------------------+
|min_ram          |xsd:int       |The minimum amount of RAM in MB that is      |
|                 |*(Required)*  |required to boot the image. The value might  |
|                 |              |be ``null`` (JSON null data type).           |
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
|owner            |csapi:UUID    |The ID of the owner, or tenant, of the       |
|                 |*(Required)*  |image. The value might be ``null`` (JSON     |
|                 |              |null data type).                             |
+-----------------+--------------+---------------------------------------------+
|min_disk         |xsd:int       |The minimum disk size in GB that is required |
|                 |*(Required)*  |to boot the image. The value might be        |
|                 |              |``null`` (JSON null data type).              |
+-----------------+--------------+---------------------------------------------+
|tags             |xsd:list      |A list of ``tag`` objects.                   |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|locations        |xsd:list      |A list of URLs to access the image file in   |
|                 |*(Required)*  |external store. This list appears if the     |
|                 |              |``show_multiple_locations`` option is set to |
|                 |              |``True`` in the Image service's              |
|                 |              |configuration file.                          |
+-----------------+--------------+---------------------------------------------+
|visibility       |xsd:string    |The image visibility. A valid value is       |
|                 |*(Required)*  |``public`` or ``private``. Default is        |
|                 |              |``private``.                                 |
+-----------------+--------------+---------------------------------------------+
|id               |csapi:UUID    |The UUID of the image.                       |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|size             |xsd:int       |The size of the image data, in bytes. The    |
|                 |*(Required)*  |value might be ``null`` (JSON null data      |
|                 |              |type).                                       |
+-----------------+--------------+---------------------------------------------+
|virtual_size     |xsd:int       |The virtual size of the image. The value     |
|                 |*(Required)*  |might be ``null`` (JSON null data type).     |
+-----------------+--------------+---------------------------------------------+
|name             |xsd:string    |The name of the image. Value might be        |
|                 |*(Required)*  |``null`` (JSON null data type).              |
+-----------------+--------------+---------------------------------------------+
|checksum         |xsd:string    |Hash that is used over the the image data.   |
|                 |*(Required)*  |The Image service uses this value for        |
|                 |              |verification. The value might be ``null``    |
|                 |              |(JSON null data type).                       |
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
|properties       |xsd:dict      |The image properties, if any.                |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|protected        |xsd:boolean   |Image protection for deletion. A valid value |
|                 |*(Required)*  |is ``True`` or ``False``. Default is         |
|                 |              |``False``.                                   |
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





**Example Create Image: JSON request**


.. code::

    {
        "status": "queued",
        "name": "Ubuntu",
        "tags": [],
        "container_format": "bare",
        "created_at": "2015-11-29T22:21:42Z",
        "size": null,
        "disk_format": "raw",
        "updated_at": "2015-11-29T22:21:42Z",
        "visibility": "private",
        "locations": [],
        "self": "/v2/images/b2173dd3-7ad6-4362-baa6-a68bce3565cb",
        "min_disk": 0,
        "protected": false,
        "id": "b2173dd3-7ad6-4362-baa6-a68bce3565cb",
        "file": "/v2/images/b2173dd3-7ad6-4362-baa6-a68bce3565cb/file",
        "checksum": null,
        "owner": "bab7d5c60cd041a0a36f7c4b6e1dd978",
        "virtual_size": null,
        "min_ram": 0,
        "schema": "/v2/schemas/image"
    }
    

