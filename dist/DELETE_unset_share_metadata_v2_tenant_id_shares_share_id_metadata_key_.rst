=============================================================================
Unset Share Metadata -  OpenStack Compute API v2.1
=============================================================================

Unset Share Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_unset_share_metadata_v2_tenant_id_shares_share_id_metadata_key_.rst#request>`__
`Response <DELETE_unset_share_metadata_v2_tenant_id_shares_share_id_metadata_key_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/shares/{share_id}/metadata/{key}

Unsets the metadata on a share.

To unset a metadata key value, specify only the key name in the URI.



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
|{metadata_key}            |csapi:string             |The metadata key.        |
+--------------------------+-------------------------+-------------------------+
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








Response
^^^^^^^^^^^^^^^^^^




