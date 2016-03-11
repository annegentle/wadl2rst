=============================================================================
List Extra Specs -  OpenStack Compute API v2.1
=============================================================================

List Extra Specs
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_extra_specs_v2_tenant_id_types_share_type_id_extra_specs.rst#request>`__
`Response <GET_list_extra_specs_v2_tenant_id_types_share_type_id_extra_specs.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/types/{share_type_id}/extra_specs

Lists the extra specifications for a share type.



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

+-----------------------------+------------------------+-----------------------+
|Name                         |Type                    |Description            |
+=============================+========================+=======================+
|extra_specs                  |xsd:dict *(Required)*   |The extra              |
|                             |                        |specifications for the |
|                             |                        |share type.            |
+-----------------------------+------------------------+-----------------------+
|driver_handles_share_servers |xsd:bool *(Required)*   |An extra specification |
|                             |                        |that defines the       |
|                             |                        |driver mode for share  |
|                             |                        |server, or storage,    |
|                             |                        |life cycle management. |
|                             |                        |The Shared File        |
|                             |                        |Systems service        |
|                             |                        |creates a share server |
|                             |                        |for the export of      |
|                             |                        |shares. This value is  |
|                             |                        |``true`` when the      |
|                             |                        |share driver manages,  |
|                             |                        |or handles, the share  |
|                             |                        |server life cycle.     |
|                             |                        |This value is          |
|                             |                        |``false`` when an      |
|                             |                        |administrator rather   |
|                             |                        |than a share driver    |
|                             |                        |manages the storage    |
|                             |                        |life cycle.            |
+-----------------------------+------------------------+-----------------------+
|snapshot_support             |xsd:bool *(Required)*   |An extra specification |
|                             |                        |that filters back ends |
|                             |                        |by whether they do or  |
|                             |                        |do not support share   |
|                             |                        |snapshots.             |
+-----------------------------+------------------------+-----------------------+





**Example List Extra Specs: JSON request**


.. code::

    {"extra_specs": {"snapshot_support": "True","driver_handles_share_servers": "True"}}

