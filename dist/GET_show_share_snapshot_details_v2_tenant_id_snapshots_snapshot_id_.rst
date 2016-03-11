=============================================================================
Show Share Snapshot Details -  OpenStack Compute API v2.1
=============================================================================

Show Share Snapshot Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_share_snapshot_details_v2_tenant_id_snapshots_snapshot_id_.rst#request>`__
`Response <GET_show_share_snapshot_details_v2_tenant_id_snapshots_snapshot_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/snapshots/{snapshot_id}

Shows details for a share snapshot.



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
|{snapshot_id}             |csapi:UUID               |The UUID of the snapshot.|
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

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|id              |csapi:UUID     |The UUID of the snapshot.                    |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|status          |xsd:string     |The snapshot status, which is ``available``, |
|                |*(Required)*   |``error``, ``creating``, ``deleting``, or    |
|                |               |``error_deleting``.                          |
+----------------+---------------+---------------------------------------------+
|share_id        |csapi:UUID     |The UUID of the source share that was used   |
|                |*(Required)*   |to create the snapshot.                      |
+----------------+---------------+---------------------------------------------+
|name            |xsd:string     |The snapshot name.                           |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|description     |xsd:string     |The snapshot description.                    |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|created_at      |xsd:dateTime   |The date and time stamp when the snapshot    |
|                |*(Required)*   |was created. The date and time stamp format  |
|                |               |is `ISO 8601                                 |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+
|share_proto     |xsd:string     |The file system protocol of a share          |
|                |*(Required)*   |snapshot. A valid value is ``NFS``,          |
|                |               |``CIFS``, ``GlusterFS``, or ``HDFS``.        |
+----------------+---------------+---------------------------------------------+
|share_size      |xsd:int        |The size of a source share, in GBs.          |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|size            |xsd:int        |The snapshot size, in GBs.                   |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+





**Example Show Share Snapshot Details: JSON request**


.. code::

    {"snapshot": {"status": "available","share_id": "406ea93b-32e9-4907-a117-148b3945749f","name": "snapshot_share1","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "bookmark"}],"created_at": "2015-09-07T11:50:39.000000","description": "Here is a snapshot of share Share1","share_proto": "NFS","share_size": 1,"id": "6d221c1d-0200-461e-8d20-24b4776b9ddb","size": 1}}

