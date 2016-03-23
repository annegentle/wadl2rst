=============================================================================
List Shared Images -  OpenStack Image API v1
=============================================================================

List Shared Images
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_shared_images_v1_shared-images_owner_id_.rst#request>`__
`Response <GET_list_shared_images_v1_shared-images_owner_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/shared-images/{owner_id}

Lists the VM images that an owner shares. The owner ID is the tenant ID.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Image ID                 |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{owner_id}                |xsd:string               |Owner ID, which is the   |
|                          |                         |tenant ID.               |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

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





**Example List Shared Images: JSON request**


.. code::

    {
        "shared_images": [
            {
                "image_id": "71c675ab-d94f-49cd-a114-e12490b328d9",
                "can_share": false
            },
            {
                "...": "..."
            }
        ]
    }
    

