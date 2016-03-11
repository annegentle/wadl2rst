=============================================================================
List Share Snapshots With Details -  OpenStack Compute API v2.1
=============================================================================

List Share Snapshots With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_share_snapshots_with_details_v2_tenant_id_snapshots_detail.rst#request>`__
`Response <GET_list_share_snapshots_with_details_v2_tenant_id_snapshots_detail.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/snapshots/detail

Lists all share snapshots with details.



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





**Example List Share Snapshots With Details: JSON request**


.. code::

    {"snapshots": [{"status": "creating","share_id": "d94a8548-2079-4be0-b21c-0a887acd31ca","name": "snapshot_My_share","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/086a1aa6-c425-4ecd-9612-391a3b1b9375","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/086a1aa6-c425-4ecd-9612-391a3b1b9375","rel": "bookmark"}],"created_at": "2015-09-07T11:55:09.000000","description": "Here is a snapshot of share My_share","share_proto": "NFS","share_size": 1,"id": "086a1aa6-c425-4ecd-9612-391a3b1b9375","size": 1},{"status": "available","share_id": "406ea93b-32e9-4907-a117-148b3945749f","name": "snapshot_share1","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "bookmark"}],"created_at": "2015-09-07T11:50:39.000000","description": "Here is a snapshot of share Share1","share_proto": "NFS","share_size": 1,"id": "6d221c1d-0200-461e-8d20-24b4776b9ddb","size": 1}]}

