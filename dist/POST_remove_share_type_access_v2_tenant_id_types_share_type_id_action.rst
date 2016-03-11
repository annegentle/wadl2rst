=============================================================================
Remove Share Type Access -  OpenStack Compute API v2.1
=============================================================================

Remove Share Type Access
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_remove_share_type_access_v2_tenant_id_types_share_type_id_action.rst#request>`__
`Response <POST_remove_share_type_access_v2_tenant_id_types_share_type_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/types/{share_type_id}/action

Removes share type access from a project.

You can remove access from private share types only.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|project                   |csapi:UUID *(Required)*  |The UUID of the project  |
|                          |                         |for which access to the  |
|                          |                         |share type is denied.    |
+--------------------------+-------------------------+-------------------------+





**Example Remove Share Type Access: JSON request**


.. code::

    {"removeProjectAccess": {"project": "818a3f48dcd644909b3fa2e45a399a27"}}


Response
^^^^^^^^^^^^^^^^^^




