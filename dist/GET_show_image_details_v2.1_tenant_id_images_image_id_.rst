=============================================================================
Show Image Details -  OpenStack Compute API v2.1
=============================================================================

Show Image Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_image_details_v2.1_tenant_id_images_image_id_.rst#request>`__
`Response <GET_show_image_details_v2.1_tenant_id_images_image_id_.rst#response>`__

.. code-block:: javascript

    GET //v2.1/{tenant_id}/images/{image_id}

Shows details for an image.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|203                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{image_id}                |csapi:UUID               |The UUID of the image.   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Image Details: JSON request**


.. code::

    {
        "image": {
            "OS-EXT-IMG-SIZE:size": "74185822",
            "created": "2011-01-01T01:02:03Z",
            "id": "70a599e0-31e7-49b7-b260-868f441e862b",
            "links": [
                {
                    "href": "http://openstack.example.com/v2.1/images/70a599e0-31e7-49b7-b260-868f441e862b",
                    "rel": "self"
                },
                {
                    "href": "http://openstack.example.com/images/70a599e0-31e7-49b7-b260-868f441e862b",
                    "rel": "bookmark"
                },
                {
                    "href": "http://glance.openstack.example.com/images/70a599e0-31e7-49b7-b260-868f441e862b",
                    "rel": "alternate",
                    "type": "application/vnd.openstack.image"
                }
            ],
            "metadata": {
                "architecture": "x86_64",
                "auto_disk_config": "True",
                "kernel_id": "nokernel",
                "ramdisk_id": "nokernel"
            },
            "minDisk": 0,
            "minRam": 0,
            "name": "fakeimage7",
            "progress": 100,
            "status": "ACTIVE",
            "updated": "2011-01-01T01:02:03Z"
        }
    }
    

