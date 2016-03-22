=============================================================================
List Images -  OpenStack Compute API v2.1
=============================================================================

List Images
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_images_v2_tenant_id_images_detail.rst#request>`__
`Response <GET_list_images_v2_tenant_id_images_detail.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/images/detail

Lists images with details.



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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-disk-config:diskConfig |xsd:string               |Valid value is ``AUTO``  |
|                          |                         |or ``MANUAL``.           |
+--------------------------+-------------------------+-------------------------+





**Example List Images: JSON request**


.. code::

    

