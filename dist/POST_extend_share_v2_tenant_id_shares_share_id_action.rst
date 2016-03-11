=============================================================================
Extend Share -  OpenStack Compute API v2.1
=============================================================================

Extend Share
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_extend_share_v2_tenant_id_shares_share_id_action.rst#request>`__
`Response <POST_extend_share_v2_tenant_id_shares_share_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/shares/{share_id}/action

Increases the size of a share.



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
|new_size                  |xsd:int *(Required)*     |New size of the share,   |
|                          |                         |in GBs.                  |
+--------------------------+-------------------------+-------------------------+





**Example Extend Share: JSON request**


.. code::

    {"os-extend": {"new_size": 2}}


Response
^^^^^^^^^^^^^^^^^^




