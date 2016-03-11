=============================================================================
Show Share Type Access Details -  OpenStack Compute API v2.1
=============================================================================

Show Share Type Access Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_share_type_access_details_v2_tenant_id_types_share_type_id_os-share-type-access.rst#request>`__
`Response <GET_show_share_type_access_details_v2_tenant_id_types_share_type_id_os-share-type-access.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/types/{share_type_id}/os-share-type-access

Shows access details for a share type.

You can view access details for private share types only.



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
|{share_type_id}           |csapi:UUID               |The UUID of the share    |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|X-Openstack-Manila-Api-   |xsd:string               |The HTTP header to       |
|Version                   |                         |specify a valid Shared   |
|                          |                         |File Systems API micro-  |
|                          |                         |version. For example,    |
|                          |                         |``"X-Openstack-Manila-   |
|                          |                         |Api-Version: 2.6"``. If  |
|                          |                         |you omit this header,    |
|                          |                         |the default micro-       |
|                          |                         |version is 2.0.          |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|share_type_id             |csapi:UUID *(Required)*  |The UUID of the share    |
|                          |                         |type to which you        |
|                          |                         |granted access.          |
+--------------------------+-------------------------+-------------------------+
|project_id                |csapi:UUID *(Required)*  |The UUID of the project  |
|                          |                         |for which access to the  |
|                          |                         |share type is granted.   |
+--------------------------+-------------------------+-------------------------+





**Example Show Share Type Access Details: JSON request**


.. code::

    {"share_type_access": [{"share_type_id": "1732f284-401d-41d9-a494-425451e8b4b8","project_id": "818a3f48dcd644909b3fa2e45a399a27"},{"share_type_id": "1732f284-401d-41d9-a494-425451e8b4b8","project_id": "e1284adea3ee4d2482af5ed214f3ad90"}]}

