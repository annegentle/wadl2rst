=============================================================================
Unset An Extra Spec -  OpenStack Compute API v2.1
=============================================================================

Unset An Extra Spec
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_unset_an_extra_spec_v2_tenant_id_types_share_type_id_extra_specs_key_.rst#request>`__
`Response <DELETE_unset_an_extra_spec_v2_tenant_id_types_share_type_id_extra_specs_key_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/types/{share_type_id}/extra_specs/{key}

Unsets an extra specification for the share type.



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
|{extra-spec-key}          |csapi:string             |The extra specification  |
|                          |                         |key.                     |
+--------------------------+-------------------------+-------------------------+
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




