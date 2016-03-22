=============================================================================
Show Image Details -  OpenStack Compute API v2.1
=============================================================================

Show Image Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_image_details_v2_tenant_id_images_image_id_.rst#request>`__
`Response <GET_show_image_details_v2_tenant_id_images_image_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/images/{image_id}

Shows details for an image.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{image_id}                |csapi:UUID               |The UUID of the image.   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-disk-config:diskConfig |xsd:string               |Valid value is ``AUTO``  |
|                          |                         |or ``MANUAL``.           |
+--------------------------+-------------------------+-------------------------+





**Example Show Image Details: JSON request**


.. code::

    

