=============================================================================
Manage Share -  OpenStack Compute API v2.1
=============================================================================

Manage Share
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_manage_share_v2_tenant_id_os-share-manage.rst#request>`__
`Response <POST_manage_share_v2_tenant_id_os-share-manage.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/os-share-manage

Configures Shared File Systems to manage a share.



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

+-------------------+------------------+---------------------------------------+
|Name               |Type              |Description                            |
+===================+==================+=======================================+
|share              |xsd:dict          |A ``share`` object.                    |
|                   |*(Required)*      |                                       |
+-------------------+------------------+---------------------------------------+
|protocol           |xsd:string        |The Shared File Systems protocol of    |
|                   |*(Required)*      |the share to manage. A valid value is  |
|                   |                  |``NFS``, ``CIFS``, ``GlusterFS``, or   |
|                   |                  |``HDFS``.                              |
+-------------------+------------------+---------------------------------------+
|name               |xsd:string        |The share name.                        |
|                   |*(Required)*      |                                       |
+-------------------+------------------+---------------------------------------+
|share_type         |xsd:string        |The share type name.                   |
|                   |*(Required)*      |                                       |
+-------------------+------------------+---------------------------------------+
|driver_options     |xsd:dict          |A set of one or more key and value     |
|                   |*(Required)*      |pairs, as a dictionary of strings,     |
|                   |                  |that describe driver options.          |
+-------------------+------------------+---------------------------------------+
|export_path        |xsd:string        |The share export path in the format    |
|                   |*(Required)*      |appropriate for the protocol: NFS      |
|                   |                  |protocol. ``10.0.0.1:/foo_path``. For  |
|                   |                  |example, ``10.254.0.5:/shares/share-   |
|                   |                  |42033c24-0261-424f-abda-               |
|                   |                  |4fef2f6dbfd5``. CIFS protocol.         |
|                   |                  |``\\10.0.0.1\foo_name_of_cifs_share``. |
+-------------------+------------------+---------------------------------------+
|service_host       |xsd:string        |The manage-share service host in this  |
|                   |*(Required)*      |format: ``host@backend#POOL``.         |
|                   |                  |``host``. The host name for the back   |
|                   |                  |end. ``backend``. The name of the back |
|                   |                  |end. ``POOL``. The pool name for the   |
|                   |                  |back end.                              |
+-------------------+------------------+---------------------------------------+
|description        |xsd:string        |The share description.                 |
|                   |*(Required)*      |                                       |
+-------------------+------------------+---------------------------------------+





**Example Manage Share: JSON request**


.. code::

    {"share": {"protocol": "nfs","name": "share_texas1","share_type": "d","driver_options": {"opt1": "opt1","opt2": "opt2"},"export_path": "10.254.0.5:/shares/share-42033c24-0261-424f-abda-4fef2f6dbfd5","service_host": "manila2@unmanage1#UNMANAGE1","description": "Lets manage share."}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------------------+-------------+---------------------------------------------+
|Name                        |Type         |Description                                  |
+============================+=============+=============================================+
|share                       |xsd:dict     |A ``share`` object.                          |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|links                       |xsd:list     |The share links.                             |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|availability_zone           |xsd:string   |The availability zone.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|share_network_id            |csapi:UUID   |The UUID of the share network.               |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|export_locations            |xsd:list     |A list of export locations. For example,     |
|                            |*(Required)* |when a share server has more than one        |
|                            |             |network interface, it can have multiple      |
|                            |             |export locations.                            |
+----------------------------+-------------+---------------------------------------------+
|share_server_id             |csapi:UUID   |The UUID of the share server.                |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|snapshot_id                 |csapi:UUID   |The UUID of the snapshot.                    |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|id                          |csapi:UUID   |The UUID of the share.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|size                        |xsd:int      |The share size, in GBs.                      |
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
|export_location             |xsd:string   |The export location.                         |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|consistency_group_id        |csapi:UUID   |(Since API v2.4.) The UUID of the            |
|                            |*(Required)* |consistency group where the share was        |
|                            |             |created.                                     |
+----------------------------+-------------+---------------------------------------------+
|project_id                  |csapi:UUID   |The UUID of the project where the share was  |
|                            |*(Required)* |created.                                     |
+----------------------------+-------------+---------------------------------------------+
|metadata                    |xsd:dict     |One or more metadata key and value pairs as  |
|                            |*(Required)* |a dictionary of strings.                     |
+----------------------------+-------------+---------------------------------------------+
|status                      |xsd:string   |The share status, which is ``available``,    |
|                            |*(Required)* |``manage_starting``, or ``manage_error``.    |
+----------------------------+-------------+---------------------------------------------+
|description                 |xsd:string   |The share description.                       |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|host                        |xsd:string   |The share host name.                         |
|                            |*(Required)* |                                             |
+----------------------------+-------------+---------------------------------------------+
|is_public                   |xsd:bool     |The level of visibility for the share.       |
|                            |*(Required)* |Defines whether other tenants can or cannot  |
|                            |             |see the share.                               |
+----------------------------+-------------+---------------------------------------------+
|snapshot_support            |xsd:bool     |(Since API v2.2.) An extra specification     |
|                            |*(Required)* |that filters back ends by whether they do or |
|                            |             |do not support share snapshots.              |
+----------------------------+-------------+---------------------------------------------+
|name                        |xsd:string   |The share name.                              |
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
|share_proto                 |xsd:string   |The Shared File Systems protocol. A valid    |
|                            |*(Required)* |value is ``NFS``, ``CIFS``, ``GlusterFS``,   |
|                            |             |or ``HDFS``.                                 |
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





**Example Manage Share: JSON request**


.. code::

    {"share": {"links": [{"href": "http://172.18.198.54:8786/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares/00137b40-ca06-4ae8-83a3-2c5989eebcce","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/00137b40-ca06-4ae8-83a3-2c5989eebcce","rel": "bookmark"}],"availability_zone": null,"share_network_id": null,"export_locations": [],"share_server_id": null,"snapshot_id": null,"id": "00137b40-ca06-4ae8-83a3-2c5989eebcce","size": null,"share_type": "14747856-08e5-494f-ab40-a64b9d20d8f7","share_type_name": "d","export_location": "10.254.0.5:/shares/share-42033c24-0261-424f-abda-4fef2f6dbfd5","consistency_group_id": null,"project_id": "16e1ab15c35a457e9c2b2aa189f544e1","metadata": {},"status": "manage_starting","description": "Lets manage share.","host": "manila2@unmanage1#UNMANAGE1","is_public": false,"snapshot_support": true,"name": "share_texas1","created_at": "2015-09-17T16:21:12.000000","share_proto": "NFS","volume_type": "d","source_cgsnapshot_member_id": null}}

