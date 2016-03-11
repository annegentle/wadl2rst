=============================================================================
List Back-End Storage Pools With Details -  OpenStack Compute API v2.1
=============================================================================

List Back-End Storage Pools With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_back-end_storage_pools_with_details_v2_tenant_id_scheduler-stats_pools_detail.rst#request>`__
`Response <GET_list_back-end_storage_pools_with_details_v2_tenant_id_scheduler-stats_pools_detail.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/scheduler-stats/pools/detail

Lists all storage pools for a back end, with details.



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

+-----------------------------+-------------+---------------------------------------------+
|Name                         |Type         |Description                                  |
+=============================+=============+=============================================+
|backend                      |xsd:string   |The name of the back end.                    |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|host                         |xsd:string   |The host name for the back end.              |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|pool                         |xsd:string   |The pool name for the back end.              |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|name                         |xsd:string   |The name of the back end in this format:     |
|                             |*(Required)* |``host@backend#POOL``. ``host``. The host    |
|                             |             |name for the back end. ``backend``. The name |
|                             |             |of the back end. ``POOL``. The pool name for |
|                             |             |the back end.                                |
+-----------------------------+-------------+---------------------------------------------+
|capabilities                 |xsd:dict     |The capabilities for the storage back end.   |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|QoS_support                  |xsd:bool     |The quality of service (QoS) support.        |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|consistency_group_support    |xsd:string   |(Since API v2.4.) The consistency group      |
|                             |*(Required)* |support. A valid value is: ``pool`` or       |
|                             |             |``host``. Consistency groups are supported.  |
|                             |             |Specifies the level of consistency groups    |
|                             |             |support. ``false``. Consistency groups are   |
|                             |             |not supported.                               |
+-----------------------------+-------------+---------------------------------------------+
|timestamp                    |xsd:dateTime |The date and time stamp when the API request |
|                             |*(Required)* |was issued. The date and time stamp format   |
|                             |             |is `ISO 8601                                 |
|                             |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                             |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                             |             |value, if included, returns the time zone as |
|                             |             |an offset from UTC. For example, ``2015-08-  |
|                             |             |27T09:49:58-05:00``.                         |
+-----------------------------+-------------+---------------------------------------------+
|share_backend_name           |xsd:string   |The name of the share back end.              |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|server_pools_mapping         |xsd:dict     |The mapping between servers and pools.       |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|driver_handles_share_servers |xsd:bool     |An extra specification that defines the      |
|                             |*(Required)* |driver mode for share server, or storage,    |
|                             |             |life cycle management. The Shared File       |
|                             |             |Systems service creates a share server for   |
|                             |             |the export of shares. This value is ``true`` |
|                             |             |when the share driver manages, or handles,   |
|                             |             |the share server life cycle. This value is   |
|                             |             |``false`` when an administrator rather than  |
|                             |             |a share driver manages the storage life      |
|                             |             |cycle.                                       |
+-----------------------------+-------------+---------------------------------------------+
|driver_version               |xsd:string   |The driver version.                          |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|total_capacity_gb            |xsd:string   |The total capacity for the back end, in GBs. |
|                             |*(Required)* |A valid value is a string, such as           |
|                             |             |``unknown``, or an integer.                  |
+-----------------------------+-------------+---------------------------------------------+
|free_capacity_gb             |xsd:string   |The amount of free capacity for the back     |
|                             |*(Required)* |end, in GBs. A valid value is a string, such |
|                             |             |as ``unknown``, or an integer.               |
+-----------------------------+-------------+---------------------------------------------+
|reserved_percentage          |xsd:int      |The percentage of the total capacity that is |
|                             |*(Required)* |reserved for the internal use by the back    |
|                             |             |end.                                         |
+-----------------------------+-------------+---------------------------------------------+
|pools                        |xsd:string   |The pools for the back end. This value is    |
|                             |*(Required)* |either ``null`` or a string value that       |
|                             |             |indicates the capabilities for each pool.    |
|                             |             |For example, ``pool_name``,                  |
|                             |             |``total_capacity_gb``, ``QoS_support``, and  |
|                             |             |so on.                                       |
+-----------------------------+-------------+---------------------------------------------+
|vendor_name                  |xsd:string   |The name of the vendor for the back end.     |
|                             |*(Required)* |                                             |
+-----------------------------+-------------+---------------------------------------------+
|snapshot_support             |xsd:bool     |The specification that filters back ends by  |
|                             |*(Required)* |whether they do or do not support share      |
|                             |             |snapshots.                                   |
+-----------------------------+-------------+---------------------------------------------+
|storage_protocol             |xsd:bool     |The storage protocol for the back end. For   |
|                             |*(Required)* |example, ``NFS_CIFS``, ``glusterfs``,        |
|                             |             |``HDFS``, and so on.                         |
+-----------------------------+-------------+---------------------------------------------+





**Example List Back-End Storage Pools With Details: JSON request**


.. code::

    {"pools": [{"pool": "LONDON","host": "nosb-devstack","name": "nosb-devstack@london#LONDON","capabilities": {"QoS_support": false,"consistency_group_support": "pool","timestamp": "2015-09-21T08:58:56.190856","share_backend_name": "LONDON","server_pools_mapping": {"1320689d-80f4-49f6-8a70-0e2c1ed8ad90": [],"3a4caac5-0880-4629-a334-6cdda88a0c0e": []},"driver_handles_share_servers": true,"driver_version": "1.0","total_capacity_gb": "unknown","reserved_percentage": 0,"pools": null,"vendor_name": "Open Source","snapshot_support": true,"free_capacity_gb": "unknown","storage_protocol": "NFS_CIFS"},"backend": "london"}]}

