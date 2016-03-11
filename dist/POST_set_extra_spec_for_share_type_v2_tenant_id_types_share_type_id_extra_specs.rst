=============================================================================
Set Extra Spec For Share Type -  OpenStack Compute API v2.1
=============================================================================

Set Extra Spec For Share Type
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_set_extra_spec_for_share_type_v2_tenant_id_types_share_type_id_extra_specs.rst#request>`__
`Response <POST_set_extra_spec_for_share_type_v2_tenant_id_types_share_type_id_extra_specs.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/types/{share_type_id}/extra_specs

Sets an extra specification for the share type.

Each driver implementation determines which extra specification keys it uses. For details, see `Capabilities and Extra-Specs <http://docs.openstack.org/developer/manila/devref/capabilities_and_extra_specs.html>`__ and documentation for your driver.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|extra_specs               |xsd:dict *(Required)*    |Extra specifications for |
|                          |                         |the share type.          |
+--------------------------+-------------------------+-------------------------+





**Example Set Extra Spec For Share Type: JSON request**


.. code::

    {"extra_specs": {"my_key": "my_value"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|extra_specs               |xsd:dict *(Required)*    |Extra specifications for |
|                          |                         |the share type.          |
+--------------------------+-------------------------+-------------------------+





**Example Set Extra Spec For Share Type: JSON request**


.. code::

    {"extra_specs": {"my_key": "my_value"}}

