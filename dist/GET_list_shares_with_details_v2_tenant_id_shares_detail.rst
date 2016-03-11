=============================================================================
List Shares With Details -  OpenStack Compute API v2.1
=============================================================================

List Shares With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_shares_with_details_v2_tenant_id_shares_detail.rst#request>`__
`Response <GET_list_shares_with_details_v2_tenant_id_shares_detail.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/shares/detail

Lists all shares, with details.



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



This table shows the query parameters for the request:

+---------------------+---------------+----------------------------------------+
|Name                 |Type           |Description                             |
+=====================+===============+========================================+
|all_tenants          |xsd:bool       |(Admin only). Defines whether to list   |
|                     |*(Required)*   |shares for all tenants. Set to ``1`` to |
|                     |               |list shares for all tenants. Set to     |
|                     |               |``0`` to list shares only for the       |
|                     |               |current tenant.                         |
+---------------------+---------------+----------------------------------------+
|name                 |xsd:string     |The share name.                         |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|status               |xsd:string     |Filters by a share status. A valid      |
|                     |*(Required)*   |value is ``creating``, ``error``,       |
|                     |               |``available``, ``deleting``,            |
|                     |               |``error_deleting``,                     |
|                     |               |``manage_starting``, ``manage_error``,  |
|                     |               |``unmanage_starting``,                  |
|                     |               |``unmanage_error``, ``unmanaged``,      |
|                     |               |``extending``, ``extending_error``,     |
|                     |               |``shrinking``, ``shrinking_error``, or  |
|                     |               |``shrinking_possible_data_loss_error``. |
+---------------------+---------------+----------------------------------------+
|share_server_id      |csapi:UUID     |The UUID of the share server.           |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|metadata             |xsd:dict       |One or more metadata key-value pairs,   |
|                     |*(Required)*   |as a dictionary of strings.             |
+---------------------+---------------+----------------------------------------+
|extra_specs          |xsd:string     |The extra specifications as a set of    |
|                     |*(Required)*   |one or more key-value pairs. In each    |
|                     |               |pair, the key is the name of the extra  |
|                     |               |specification and the value is the      |
|                     |               |share type that was used to create the  |
|                     |               |share.                                  |
+---------------------+---------------+----------------------------------------+
|share_type_id        |csapi:UUID     |(Since API v2.6.) The UUID of the share |
|                     |*(Required)*   |type.                                   |
+---------------------+---------------+----------------------------------------+
|limit                |xsd:int        |The maximum number of shares to return. |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|offset               |xsd:int        |The offset to define start point of     |
|                     |*(Required)*   |share listing.                          |
+---------------------+---------------+----------------------------------------+
|sort_key             |xsd:string     |The key to sort a list of shares. A     |
|                     |*(Required)*   |valid value is ``id``, ``status``,      |
|                     |               |``size``, ``host``, ``share_proto``,    |
|                     |               |``export_location``,                    |
|                     |               |``availability_zone``, ``user_id``,     |
|                     |               |``project_id``, ``created_at``,         |
|                     |               |``updated_at``, ``display_name``,       |
|                     |               |``name``, ``share_type_id``,            |
|                     |               |``share_type``, ``share_network_id``,   |
|                     |               |``share_network``, ``snapshot_id``, or  |
|                     |               |``snapshot``.                           |
+---------------------+---------------+----------------------------------------+
|sort_dir             |xsd:string     |The direction to sort a list of shares. |
|                     |*(Required)*   |A valid value is ``asc``, or ``desc``.  |
+---------------------+---------------+----------------------------------------+
|snapshot_id          |csapi:UUID     |The UUID of the snapshot that was used  |
|                     |*(Required)*   |to create the share.                    |
+---------------------+---------------+----------------------------------------+
|host                 |xsd:string     |The share host name.                    |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|share_network_id     |csapi:UUID     |The UUID of the share network.          |
|                     |*(Required)*   |                                        |
+---------------------+---------------+----------------------------------------+
|project_id           |csapi:UUID     |The UUID of the project in which the    |
|                     |*(Required)*   |share was created. Useful with          |
|                     |               |``all_tenants`` parameter.              |
+---------------------+---------------+----------------------------------------+
|is_public            |xsd:bool       |The level of visibility for the share.  |
|                     |*(Required)*   |Set to ``true`` to list only public     |
|                     |               |shares. Set to ``false`` to list only   |
|                     |               |private shares.                         |
+---------------------+---------------+----------------------------------------+
|consistency_group_id |csapi:UUID     |(Since API v2.4.) The UUID of the       |
|                     |*(Required)*   |consistency group where the share was   |
|                     |               |created.                                |
+---------------------+---------------+----------------------------------------+







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





**Example List Shares With Details: JSON request**


.. code::

    {"shares": [{"links": [{"href": "http://172.18.198.54:8786/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares/f45cc5b2-d1bb-4a3e-ba5b-5c4125613adc","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/f45cc5b2-d1bb-4a3e-ba5b-5c4125613adc","rel": "bookmark"}],"availability_zone": "nova","share_network_id": "f9b2e754-ac01-4466-86e1-5c569424754e","export_locations": [],"share_server_id": "87d8943a-f5da-47a4-b2f2-ddfa6794aa82","snapshot_id": null,"id": "f45cc5b2-d1bb-4a3e-ba5b-5c4125613adc","size": 1,"share_type": "25747776-08e5-494f-ab40-a64b9d20d8f7","share_type_name": "default","export_location": null,"consistency_group_id": "9397c191-8427-4661-a2e8-b23820dc01d4","project_id": "16e1ab15c35a457e9c2b2aa189f544e1","metadata": {},"status": "error","description": "There is a share description.","host": "manila2@generic1#GENERIC1","task_state": null,"is_public": true,"snapshot_support": true,"name": "my_share4","created_at": "2015-09-16T18:19:50.000000","share_proto": "NFS","volume_type": "default","source_cgsnapshot_member_id": null},{"links": [{"href": "http://172.18.198.54:8786/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares/c4a2ced4-2c9f-4ae1-adaa-6171833e64df","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/c4a2ced4-2c9f-4ae1-adaa-6171833e64df","rel": "bookmark"}],"availability_zone": "nova","share_network_id": "f9b2e754-ac01-4466-86e1-5c569424754e","export_locations": ["10.254.0.5:/shares/share-50ad5e7b-f6f1-4b78-a651-0812cef2bb67"],"share_server_id": "87d8943a-f5da-47a4-b2f2-ddfa6794aa82","snapshot_id": null,"id": "c4a2ced4-2c9f-4ae1-adaa-6171833e64df","size": 1,"share_type": "25747776-08e5-494f-ab40-a64b9d20d8f7","share_type_name": "default","export_location": "10.254.0.5:/shares/share-50ad5e7b-f6f1-4b78-a651-0812cef2bb67","consistency_group_id": "9397c191-8427-4661-a2e8-b23820dc01d4","project_id": "16e1ab15c35a457e9c2b2aa189f544e1","metadata": {},"status": "available","description": "Changed description.","host": "manila2@generic1#GENERIC1","task_state": null,"is_public": true,"snapshot_support": true,"name": "my_share4","created_at": "2015-09-16T17:26:28.000000","share_proto": "NFS","volume_type": "default","source_cgsnapshot_member_id": null}]}

