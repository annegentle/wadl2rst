=============================================================================
Update Share Metadata -  OpenStack Compute API v2.1
=============================================================================

Update Share Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_share_metadata_v2_tenant_id_shares_share_id_metadata.rst#request>`__
`Response <PUT_update_share_metadata_v2_tenant_id_shares_share_id_metadata.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/shares/{share_id}/metadata

Updates the metadata for a share.



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
|metadata                  |xsd:dict *(Required)*    |One or more metadata key-|
|                          |                         |value pairs, as a        |
|                          |                         |dictionary of strings.   |
|                          |                         |For example,             |
|                          |                         |``"project": "my_test",  |
|                          |                         |"aim": "testing"``. The  |
|                          |                         |share server does not    |
|                          |                         |respect case-sensitive   |
|                          |                         |key names. For example,  |
|                          |                         |``"key": "v1"`` and      |
|                          |                         |``"KEY": "V1"`` are      |
|                          |                         |equivalent. If you       |
|                          |                         |specify both key-value   |
|                          |                         |pairs, the server sets   |
|                          |                         |and returns only the     |
|                          |                         |``"KEY": "V1"`` key-     |
|                          |                         |value pair.              |
+--------------------------+-------------------------+-------------------------+





**Example Update Share Metadata: JSON request**


.. code::

    {"metadata": {"aim": "changed_doc","project": "my_app","new_metadata_key": "new_information"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|metadata                  |xsd:dict *(Required)*    |One or more metadata key |
|                          |                         |and value pairs as a     |
|                          |                         |dictionary of strings.   |
+--------------------------+-------------------------+-------------------------+





**Example Update Share Metadata: JSON request**


.. code::

    {"metadata": {"aim": "changed_doc","project": "my_app","new_metadata_key": "new_information"}}

