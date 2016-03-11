=============================================================================
Set Share Metadata -  OpenStack Compute API v2.1
=============================================================================

Set Share Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_set_share_metadata_v2_tenant_id_shares_share_id_metadata.rst#request>`__
`Response <POST_set_share_metadata_v2_tenant_id_shares_share_id_metadata.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/shares/{share_id}/metadata

Sets the metadata on a share.



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





**Example Set Share Metadata: JSON request**


.. code::

    {"metadata": {"key1": "value1"}}


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





**Example Set Share Metadata: JSON request**


.. code::

    {"metadata": {"aim": "changed_doc","project": "my_app","key1": "value1","new_metadata_key": "new_information","key": "value"}}

