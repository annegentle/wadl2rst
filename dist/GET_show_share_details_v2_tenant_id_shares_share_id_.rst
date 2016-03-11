=============================================================================
Show Share Details -  OpenStack Compute API v2.1
=============================================================================

Show Share Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_share_details_v2_tenant_id_shares_share_id_.rst#request>`__
`Response <GET_show_share_details_v2_tenant_id_shares_share_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/shares/{share_id}

Shows details for a share.



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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------------------+-------------+---------------------------------------------+
|Name                        |Type         |Description                                  |
+============================+=============+=============================================+
|id                          |csapi:UUID   |The UUID of the share.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|status                      |xsd:string   |The share status, which is ``creating``,     |
|                            |*(Required)* |``error``, ``available``, ``deleting``,      |
|                            |             |``error_deleting``, ``manage_starting``,     |
|                            |             |``manage_error``, ``unmanage_starting``,     |
|                            |             |``unmanage_error``, ``unmanaged``,           |
|                            |             |``extending``, ``extending_error``,          |
|                            |             |``shrinking``, ``shrinking_error``, or       |
|                            |             |``shrinking_possible_data_loss_error``.      |
+----------------------------+-------------+---------------------------------------------+
|size                        |xsd:int      |The share size, in GBs.                      |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|project_id                  |csapi:UUID   |The UUID of the project where the share was  |
|                            |*(Required)* |created.                                     |
+----------------------------+-------------+---------------------------------------------+
|name                        |xsd:string   |The share name.                              |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|description                 |xsd:string   |The share description.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|share_type                  |csapi:UUID   |(Since API v2.6.) The UUID of the share      |
|                            |*(Required)* |type. In minor versions, this parameter is a |
|                            |             |share type name, as a string.                |
+----------------------------+-------------+---------------------------------------------+
|share_type_name             |xsd:string   |(Since API v2.6.) The share type name. Minor |
|                            |*(Required)* |versions support only the ``share_type``     |
|                            |             |parameter where the share type name is       |
|                            |             |expected.                                    |
+----------------------------+-------------+---------------------------------------------+
|availability_zone           |xsd:string   |The availability zone.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|created_at                  |xsd:dateTime |The date and time stamp when the share was   |
|                            |*(Required)* |created. The date and time stamp format is   |
|                            |             |`ISO 8601                                    |
|                            |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                            |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                            |             |value, if included, returns the time zone as |
|                            |             |an offset from UTC. For example, ``2015-08-  |
|                            |             |27T09:49:58-05:00``.                         |
+----------------------------+-------------+---------------------------------------------+
|export_location             |xsd:string   |The export location.                         |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|export_locations            |xsd:list     |A list of export locations. For example,     |
|                            |*(Required)* |when a share server has more than one        |
|                            |             |network interface, it can have multiple      |
|                            |             |export locations.                            |
+----------------------------+-------------+---------------------------------------------+
|share_network_id            |csapi:UUID   |The UUID of the share network.               |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|share_proto                 |xsd:string   |The Shared File Systems protocol. A valid    |
|                            |*(Required)* |value is ``NFS``, ``CIFS``, ``GlusterFS``,   |
|                            |             |or ``HDFS``.                                 |
+----------------------------+-------------+---------------------------------------------+
|host                        |xsd:string   |The share host name.                         |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|volume_type                 |xsd:string   |The volume type. The use of the              |
|                            |*(Required)* |``volume_type`` object is deprecated but     |
|                            |             |supported. It is recommended that you use    |
|                            |             |the ``share_type`` object when you create a  |
|                            |             |share type. When you issue a create a share  |
|                            |             |type request, you can submit a request body  |
|                            |             |with either a ``share_type`` or              |
|                            |             |``volume_type`` object. No matter which      |
|                            |             |object type you include in the request, the  |
|                            |             |API creates both a ``volume_type`` object    |
|                            |             |and a ``share_type`` object. Both objects    |
|                            |             |have the same ID. When you issue a list      |
|                            |             |share types request, the response shows both |
|                            |             |``share_types`` and ``volume_types`` objects.|
+----------------------------+-------------+---------------------------------------------+
|snapshot_id                 |csapi:UUID   |The UUID of the snapshot.                    |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|task_state                  |xsd:string   |(Since API v2.5.) For the share migration,   |
|                            |*(Required)* |the migration task state. A valid value is   |
|                            |             |``null``, ``migration_starting``,            |
|                            |             |``migration_error``, ``migration_success``,  |
|                            |             |``migration_completing``, or ``migrating``.  |
|                            |             |The ``task_state`` is ``null`` unless the    |
|                            |             |share is migrated from one back-end to       |
|                            |             |another. For details, see ``os-              |
|                            |             |migrate_share`` extension request.           |
+----------------------------+-------------+---------------------------------------------+
|share_server_id             |csapi:UUID   |The UUID of the share server.                |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|consistency_group_id        |csapi:UUID   |(Since API v2.4.) The UUID of the            |
|                            |*(Required)* |consistency group where the share was        |
|                            |             |created.                                     |
+----------------------------+-------------+---------------------------------------------+
|snapshot_support            |xsd:bool     |(Since API v2.2.) An extra specification     |
|                            |*(Required)* |that filters back ends by whether they do or |
|                            |             |do not support share snapshots.              |
+----------------------------+-------------+---------------------------------------------+
|source_cgsnapshot_member_id |csapi:UUID   |(Since API v2.4.) If the share was created   |
|                            |*(Required)* |with ``consistency_group_id`` attribute, the |
|                            |             |snapshot member ID. The corresponding        |
|                            |             |consistency group must be created from a     |
|                            |             |snapshot with the current share as a member. |
|                            |             |Consistency groups and snapshots are the     |
|                            |             |part of the Shared File Systems experimental |
|                            |             |API. For details, see `Consistency groups    |
|                            |             |<api-ref-share-v2.html#consistency-          |
|                            |             |groups>`__ and `Consistencygroup snapshots   |
|                            |             |<api-ref-share-v2.html#consistency-group-    |
|                            |             |snapshots>`__.                               |
+----------------------------+-------------+---------------------------------------------+
|is_public                   |xsd:bool     |The level of visibility for the share.       |
|                            |*(Required)* |Defines whether other tenants can or cannot  |
|                            |             |see the share.                               |
+----------------------------+-------------+---------------------------------------------+
|metadata                    |xsd:dict     |One or more metadata key and value pairs as  |
|                            |*(Required)* |a dictionary of strings.                     |
+----------------------------+-------------+---------------------------------------------+





**Example Show Share Details: JSON request**


.. code::

    {"share": {"links": [{"href": "http://172.18.198.54:8786/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares/011d21e2-fbc3-4e4a-9993-9ea223f73264","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/011d21e2-fbc3-4e4a-9993-9ea223f73264","rel": "bookmark"}],"availability_zone": "nova","share_network_id": "713df749-aac0-4a54-af52-10f6c991e80c","export_locations": [],"share_server_id": "e268f4aa-d571-43dd-9ab3-f49ad06ffaef","snapshot_id": null,"id": "011d21e2-fbc3-4e4a-9993-9ea223f73264","size": 1,"share_type": "25747776-08e5-494f-ab40-a64b9d20d8f7","share_type_name": "default","export_location": null,"consistency_group_id": "9397c191-8427-4661-a2e8-b23820dc01d4","project_id": "16e1ab15c35a457e9c2b2aa189f544e1","metadata": {"project": "my_app","aim": "doc"},"status": "available","description": "My custom share London","host": "manila2@generic1#GENERIC1","task_state": null,"is_public": true,"snapshot_support": true,"name": "share_London","created_at": "2015-09-18T10:25:24.000000","share_proto": "NFS","volume_type": "default","source_cgsnapshot_member_id": null}}

