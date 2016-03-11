=============================================================================
Create Share Type -  OpenStack Compute API v2.1
=============================================================================

Create Share Type
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_share_type_v2_tenant_id_types.rst#request>`__
`Response <POST_create_share_type_v2_tenant_id_types.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/types

Creates a share type.



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





This table shows the body parameters for the request:

+-----------------------------+------------------------+-----------------------+
|Name                         |Type                    |Description            |
+=============================+========================+=======================+
|extra_specs                  |xsd:dict *(Required)*   |Extra specifications   |
|                             |                        |for the share type.    |
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
|                             |                        |shares. Set to         |
|                             |                        |``true`` when the      |
|                             |                        |share driver manages,  |
|                             |                        |or handles, the share  |
|                             |                        |server life cycle. Set |
|                             |                        |to ``false`` when an   |
|                             |                        |administrator rather   |
|                             |                        |than a share driver    |
|                             |                        |manages the storage    |
|                             |                        |life cycle.            |
+-----------------------------+------------------------+-----------------------+
|snapshot_support             |xsd:bool *(Required)*   |An extra specification |
|                             |                        |that filters back ends |
|                             |                        |by whether they do or  |
|                             |                        |do not support share   |
|                             |                        |snapshots. Set to      |
|                             |                        |``true`` to show back  |
|                             |                        |ends that support      |
|                             |                        |share snapshots. Set   |
|                             |                        |to ``false`` to show   |
|                             |                        |back ends that do not  |
|                             |                        |support share          |
|                             |                        |snapshots. Default is  |
|                             |                        |``true``.              |
+-----------------------------+------------------------+-----------------------+
|os-share-type-               |xsd:bool *(Required)*   |Indicates whether a    |
|access:is_public             |                        |share type is publicly |
|                             |                        |accessible. Default is |
|                             |                        |``true``, or publicly  |
|                             |                        |accessible.            |
+-----------------------------+------------------------+-----------------------+
|name                         |xsd:string *(Required)* |The share type name.   |
+-----------------------------+------------------------+-----------------------+





**Example Create Share Type: JSON request**


.. code::

    {"volume_type": {"os-share-type-access:is_public": true,"extra_specs": {"driver_handles_share_servers": true,"snapshot_support": true},"name": "my_new_volume_type"}}


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





**Example Create Share Type: JSON request**


.. code::

    {"volume_type": {"os-share-type-access:is_public": true,"required_extra_specs": {"driver_handles_share_servers": true},"extra_specs": {"snapshot_support": "True","driver_handles_share_servers": "True"},"name": "my_new_volume_type","id": "1d600d02-26a7-4b23-af3d-7d51860fe858"},"share_type": {"os-share-type-access:is_public": true,"required_extra_specs": {"driver_handles_share_servers": true},"extra_specs": {"snapshot_support": "True","driver_handles_share_servers": "True"},"name": "my_new_volume_type","id": "1d600d02-26a7-4b23-af3d-7d51860fe858"}}

