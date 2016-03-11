=============================================================================
Revoke Access -  OpenStack Compute API v2.1
=============================================================================

Revoke Access
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_revoke_access_v2_tenant_id_shares_share_id_action.rst#request>`__
`Response <POST_revoke_access_v2_tenant_id_shares_share_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/shares/{share_id}/action

Revokes access from a share.



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
|{share_id}                |csapi:UUID               |The UUID of the share.   |
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
|access_id                 |csapi:UUID *(Required)*  |The UUID of the access   |
|                          |                         |rule to which access is  |
|                          |                         |granted.                 |
+--------------------------+-------------------------+-------------------------+





**Example Revoke Access: JSON request**


.. code::

    {"os-deny_access": {"access_id": "a25b2df3-90bd-4add-afa6-5f0dbbd50452"}}


Response
^^^^^^^^^^^^^^^^^^




