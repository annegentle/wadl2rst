=============================================================================
Show Image Details And Image Binary -  OpenStack Image API v1
=============================================================================

Show Image Details And Image Binary
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_image_details_and_image_binary_v1_images_image_id_.rst#request>`__
`Response <GET_show_image_details_and_image_binary_v1_images_image_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/images/{image_id}

Shows the image details as headers and the image binary in the body of the response.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
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








Response
^^^^^^^^^^^^^^^^^^





**Example Show Image Details And Image Binary: JSON request**


.. code::

    {
        "images": [
            {
                "uri": "http://glance.example.com/images/71c675ab-d94f-49cd-a114-e12490b328d9",
                "name": "Ubuntu 10.04 Plain 5GB",
                "disk_format": "vhd",
                "container_format": "ovf",
                "size": "5368709120",
                "checksum": "c2e5db72bd7fd153f53ede5da5a06de3",
                "created_at": "2010-02-03 09:34:01",
                "updated_at": "2010-02-03 09:34:01",
                "deleted_at": "",
                "status": "active",
                "is_public": true,
                "min_ram": 256,
                "min_disk": 5,
                "owner": null,
                "properties": {
                    "distro": "Ubuntu 10.04 LTS"
                }
            },
            {
                "...": "..."
            }
        ]
    }
    

