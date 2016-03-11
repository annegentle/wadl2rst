=============================================================================
List Share Types -  OpenStack Compute API v2.1
=============================================================================

List Share Types
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_share_types_v2_tenant_id_types.rst#request>`__
`Response <GET_list_share_types_v2_tenant_id_types.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/types

Lists all share types.



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
|id                           |csapi:UUID *(Required)* |The UUID of the share  |
|                             |                        |type.                  |
+-----------------------------+------------------------+-----------------------+
|required_extra_specs         |xsd:dict *(Required)*   |The required extra     |
|                             |                        |specifications for the |
|                             |                        |share type.            |
+-----------------------------+------------------------+-----------------------+
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
|os-share-type-               |xsd:bool *(Required)*   |Indicates whether a    |
|access:is_public             |                        |share type is publicly |
|                             |                        |accessible. Default is |
|                             |                        |``true``, or publicly  |
|                             |                        |accessible.            |
+-----------------------------+------------------------+-----------------------+
|name                         |xsd:string *(Required)* |The share type name.   |
+-----------------------------+------------------------+-----------------------+





**Example List Share Types: JSON request**


.. code::

    {"volume_types": [{"os-share-type-access:is_public": true,"required_extra_specs": {"driver_handles_share_servers": "True"},"extra_specs": {"snapshot_support": "True","driver_handles_share_servers": "True"},"name": "default","id": "be27425c-f807-4500-a056-d00721db45cf"},{"os-share-type-access:is_public": true,"required_extra_specs": {"driver_handles_share_servers": "false"},"extra_specs": {"snapshot_support": "True","driver_handles_share_servers": "false"},"name": "d","id": "f015bebe-c38b-4c49-8832-00143b10253b"}],"share_types": [{"os-share-type-access:is_public": true,"required_extra_specs": {"driver_handles_share_servers": "True"},"extra_specs": {"snapshot_support": "True","driver_handles_share_servers": "True"},"name": "default","id": "be27425c-f807-4500-a056-d00721db45cf"},{"os-share-type-access:is_public": true,"required_extra_specs": {"driver_handles_share_servers": "false"},"extra_specs": {"snapshot_support": "True","driver_handles_share_servers": "false"},"name": "d","id": "f015bebe-c38b-4c49-8832-00143b10253b"}]}

