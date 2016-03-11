=============================================================================
Create Share -  OpenStack Compute API v2.1
=============================================================================

Create Share
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_share_v2_tenant_id_shares.rst#request>`__
`Response <POST_create_share_v2_tenant_id_shares.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/shares

Creates a share.



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

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|share_proto               |xsd:string *(Required)*  |The Shared File Systems  |
|                          |                         |protocol. A valid value  |
|                          |                         |is ``NFS``, ``CIFS``,    |
|                          |                         |``GlusterFS``, or        |
|                          |                         |``HDFS``.                |
+--------------------------+-------------------------+-------------------------+
|size                      |xsd:int *(Required)*     |The share size, in GBs.  |
|                          |                         |The requested share size |
|                          |                         |cannot be greater than   |
|                          |                         |the allowed GB quota. To |
|                          |                         |view the allowed quota,  |
|                          |                         |issue a get limits       |
|                          |                         |request.                 |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The share name.          |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The share description.   |
+--------------------------+-------------------------+-------------------------+
|display_name              |xsd:string *(Required)*  |The share name. The      |
|                          |                         |Shared File Systems API  |
|                          |                         |supports the use of both |
|                          |                         |``name`` and             |
|                          |                         |``display_name``         |
|                          |                         |attributes, which are    |
|                          |                         |inherited attributes     |
|                          |                         |from the Block Storage   |
|                          |                         |API.                     |
+--------------------------+-------------------------+-------------------------+
|display_description       |xsd:string *(Required)*  |The share description.   |
|                          |                         |The Shared File Systems  |
|                          |                         |API supports the use of  |
|                          |                         |both ``description`` and |
|                          |                         |``display_description``  |
|                          |                         |parameters, which are    |
|                          |                         |inherited attributes     |
|                          |                         |from the Block Storage   |
|                          |                         |API.                     |
+--------------------------+-------------------------+-------------------------+
|share_type                |xsd:string *(Required)*  |The share type name. If  |
|                          |                         |you omit this parameter, |
|                          |                         |the default share type   |
|                          |                         |is used. To view the     |
|                          |                         |default share type set   |
|                          |                         |by the administrator,    |
|                          |                         |issue a list default     |
|                          |                         |share types request. You |
|                          |                         |cannot specify both the  |
|                          |                         |``share_type`` and       |
|                          |                         |``volume_type``          |
|                          |                         |parameters.              |
+--------------------------+-------------------------+-------------------------+
|volume_type               |xsd:string *(Required)*  |The volume type. The use |
|                          |                         |of the ``volume_type``   |
|                          |                         |object is deprecated but |
|                          |                         |supported. It is         |
|                          |                         |recommended that you use |
|                          |                         |the ``share_type``       |
|                          |                         |object when you create a |
|                          |                         |share type. When you     |
|                          |                         |issue a create a share   |
|                          |                         |type request, you can    |
|                          |                         |submit a request body    |
|                          |                         |with either a            |
|                          |                         |``share_type`` or        |
|                          |                         |``volume_type`` object.  |
|                          |                         |No matter which object   |
|                          |                         |type you include in the  |
|                          |                         |request, the API creates |
|                          |                         |both a ``volume_type``   |
|                          |                         |object and a             |
|                          |                         |``share_type`` object.   |
|                          |                         |Both objects have the    |
|                          |                         |same ID. When you issue  |
|                          |                         |a list share types       |
|                          |                         |request, the response    |
|                          |                         |shows both               |
|                          |                         |``share_types`` and      |
|                          |                         |``volume_types`` objects.|
+--------------------------+-------------------------+-------------------------+
|snapshot_id               |csapi:UUID *(Required)*  |The UUID of the snapshot |
|                          |                         |from which to create the |
|                          |                         |share.                   |
+--------------------------+-------------------------+-------------------------+
|is_public                 |xsd:bool *(Required)*    |The level of visibility  |
|                          |                         |for the share. Defines   |
|                          |                         |whether other tenants    |
|                          |                         |can or cannot see the    |
|                          |                         |share.                   |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:dict *(Required)*    |One or more metadata key |
|                          |                         |and value pairs as a     |
|                          |                         |dictionary of strings.   |
+--------------------------+-------------------------+-------------------------+
|share_network_id          |csapi:UUID *(Required)*  |The UUID of a share      |
|                          |                         |network where the share  |
|                          |                         |server exists or will be |
|                          |                         |created. If              |
|                          |                         |``share_network_id`` is  |
|                          |                         |``None`` and you provide |
|                          |                         |a ``snapshot_id``, the   |
|                          |                         |``share_network_id``     |
|                          |                         |value from the snapshot  |
|                          |                         |is used.                 |
+--------------------------+-------------------------+-------------------------+
|consistency_group_id      |csapi:UUID *(Required)*  |(Since API v2.4.) The    |
|                          |                         |UUID of the available    |
|                          |                         |consistency group in     |
|                          |                         |which the share will be  |
|                          |                         |created. The consistency |
|                          |                         |group must support the   |
|                          |                         |``share_type`` and       |
|                          |                         |``share_network_id``.    |
|                          |                         |For details, see         |
|                          |                         |`Consistency groups <api-|
|                          |                         |ref-share-               |
|                          |                         |v2.html#consistency-     |
|                          |                         |groups>`__.              |
+--------------------------+-------------------------+-------------------------+
|availability_zone         |xsd:string *(Required)*  |(Since API v2.1.) The    |
|                          |                         |availability zone.       |
+--------------------------+-------------------------+-------------------------+





**Example Create Share: JSON request**


.. code::

    {"share": {"description": "My custom share London","share_type": null,"share_proto": "nfs","share_network_id": "713df749-aac0-4a54-af52-10f6c991e80c","name": "share_London","consistency_group_id": "9397c191-8427-4661-a2e8-b23820dc01d4","snapshot_id": null,"is_public": true,"size": 1,"metadata": {"project": "my_app","aim": "doc"}}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------------------+-------------+---------------------------------------------+
|Name                        |Type         |Description                                  |
+============================+=============+=============================================+
|id                          |csapi:UUID   |The UUID of the share.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|status                      |xsd:string   |The share status. A valid value is:          |
|                            |*(Required)* |``creating``. The share is being created.    |
|                            |             |``deleting``. The share is being deleted.    |
|                            |             |``error``. An error occurred during share    |
|                            |             |creation. ``error_deleting``. An error       |
|                            |             |occurred during share deletion.              |
|                            |             |``available``. The share is ready to use.    |
|                            |             |``manage_starting``. Share manage started.   |
|                            |             |``manage_error``. Share manage failed.       |
|                            |             |``unmanage_starting``. Share unmanage        |
|                            |             |started. ``unmanage_error``. Share cannot be |
|                            |             |unmanaged. ``unmanaged``. Share was          |
|                            |             |unmanaged. ``extending``. The extend, or     |
|                            |             |increase, share size request was issued      |
|                            |             |successfully. ``extending_error``. Extend    |
|                            |             |share failed. ``shrinking``. Share is being  |
|                            |             |shrunk. ``shrinking_error``. Failed to       |
|                            |             |update quota on share shrinking.             |
|                            |             |``shrinking_possible_data_loss_error``.      |
|                            |             |Shrink share failed due to possible data     |
|                            |             |loss.                                        |
+----------------------------+-------------+---------------------------------------------+
|project_id                  |csapi:UUID   |The UUID of the project in which the share   |
|                            |*(Required)* |was created.                                 |
+----------------------------+-------------+---------------------------------------------+
|share_proto                 |xsd:string   |The Shared File Systems protocol. A valid    |
|                            |*(Required)* |value is ``NFS``, ``CIFS``, ``GlusterFS``,   |
|                            |             |or ``HDFS``.                                 |
+----------------------------+-------------+---------------------------------------------+
|size                        |xsd:int      |The share size, in GBs.                      |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|name                        |xsd:string   |The share name.                              |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|description                 |xsd:string   |The share description.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|display_name                |xsd:string   |The share name. The Shared File Systems API  |
|                            |*(Required)* |supports the use of both ``name`` and        |
|                            |             |``display_name`` attributes, which are       |
|                            |             |inherited attributes from the Block Storage  |
|                            |             |API.                                         |
+----------------------------+-------------+---------------------------------------------+
|display_description         |xsd:string   |The share description. The Shared File       |
|                            |*(Required)* |Systems API supports the use of both         |
|                            |             |``description`` and ``display_description``  |
|                            |             |parameters, which are inherited attributes   |
|                            |             |from the Block Storage API.                  |
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
|snapshot_id                 |csapi:UUID   |The UUID of the snapshot from which to       |
|                            |*(Required)* |create the share.                            |
+----------------------------+-------------+---------------------------------------------+
|is_public                   |xsd:bool     |The level of visibility for the share.       |
|                            |*(Required)* |Defines whether other tenants can or cannot  |
|                            |             |see the share.                               |
+----------------------------+-------------+---------------------------------------------+
|metadata                    |xsd:dict     |One or more metadata key and value pairs as  |
|                            |*(Required)* |a dictionary of strings.                     |
+----------------------------+-------------+---------------------------------------------+
|share_network_id            |csapi:UUID   |The UUID of the share network.               |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|availability_zone           |xsd:string   |The availability zone.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|export_location             |xsd:string   |The export location.                         |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|export_locations            |xsd:list     |A list of export locations. For example,     |
|                            |*(Required)* |when a share server has more than one        |
|                            |             |network interface, it can have multiple      |
|                            |             |export locations.                            |
+----------------------------+-------------+---------------------------------------------+
|host                        |xsd:string   |The share host name.                         |
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
|created_at                  |xsd:dateTime |The date and time stamp when the share was   |
|                            |*(Required)* |created. The date and time stamp format is   |
|                            |             |`ISO 8601                                    |
|                            |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                            |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                            |             |value, if included, returns the time zone as |
|                            |             |an offset from UTC. For example, ``2015-08-  |
|                            |             |27T09:49:58-05:00``.                         |
+----------------------------+-------------+---------------------------------------------+





**Example Create Share: JSON request**


.. code::

    {"share": {"status": null,"share_server_id": null,"project_id": "16e1ab15c35a457e9c2b2aa189f544e1","name": "share_London","share_type": "25747776-08e5-494f-ab40-a64b9d20d8f7","share_type_name": "default","availability_zone": null,"created_at": "2015-09-18T10:25:24.533287","export_location": null,"links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/shares/011d21e2-fbc3-4e4a-9993-9ea223f73264","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/011d21e2-fbc3-4e4a-9993-9ea223f73264","rel": "bookmark"}],"share_network_id": null,"export_locations": [],"share_proto": "NFS","host": null,"task_state": null,"snapshot_support": true,"consistency_group_id": "9397c191-8427-4661-a2e8-b23820dc01d4","source_cgsnapshot_member_id": null,"volume_type": "default","snapshot_id": null,"is_public": true,"metadata": {"project": "my_app","aim": "doc"},"id": "011d21e2-fbc3-4e4a-9993-9ea223f73264","size": 1,"description": "My custom share London"}}

