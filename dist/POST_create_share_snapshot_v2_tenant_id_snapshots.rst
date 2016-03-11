=============================================================================
Create Share Snapshot -  OpenStack Compute API v2.1
=============================================================================

Create Share Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_share_snapshot_v2_tenant_id_snapshots.rst#request>`__
`Response <POST_create_share_snapshot_v2_tenant_id_snapshots.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/snapshots

Creates a snapshot from a share.



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
|share_id                  |csapi:UUID *(Required)*  |The UUID of the share    |
|                          |                         |from which to create a   |
|                          |                         |snapshot.                |
+--------------------------+-------------------------+-------------------------+
|force                     |xsd:bool *(Required)*    |Indicates whether        |
|                          |                         |snapshot creation is     |
|                          |                         |enabled when a share is  |
|                          |                         |busy. Set to ``true`` to |
|                          |                         |force snapshot creation  |
|                          |                         |when the share is busy.  |
|                          |                         |Set to ``false`` to deny |
|                          |                         |snapshot creation when   |
|                          |                         |the share is busy.       |
|                          |                         |Default is ``false``.    |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The snapshot name.       |
+--------------------------+-------------------------+-------------------------+
|display_name              |xsd:string *(Required)*  |The snapshot name. The   |
|                          |                         |Shared File Systems API  |
|                          |                         |supports the use of both |
|                          |                         |``name`` and             |
|                          |                         |``display_name``         |
|                          |                         |attributes, which are    |
|                          |                         |inherited attributes     |
|                          |                         |from the Block Storage   |
|                          |                         |API.                     |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The snapshot description.|
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





**Example Create Share Snapshot: JSON request**


.. code::

    {"snapshot": {"share_id": "406ea93b-32e9-4907-a117-148b3945749f","force": "True","name": "snapshot_share1","description": "Here is a snapshot of share Share1"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|id              |csapi:UUID     |The UUID of the snapshot.                    |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|share_id        |csapi:UUID     |The UUID of the source share that was used   |
|                |*(Required)*   |to create the snapshot.                      |
+----------------+---------------+---------------------------------------------+
|status          |xsd:string     |The snapshot status, which is ``available``, |
|                |*(Required)*   |``error``, ``creating``, ``deleting``, or    |
|                |               |``error_deleting``.                          |
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
|share_size      |xsd:int        |The share snapshot size, in GBs.             |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|size            |xsd:int        |The snapshot size, in GBs.                   |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+





**Example Create Share Snapshot: JSON request**


.. code::

    {"snapshot": {"status": "creating","share_id": "406ea93b-32e9-4907-a117-148b3945749f","name": "snapshot_share1","links": [{"href": "http://172.18.198.54:8786/v1/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "self"},{"href": "http://172.18.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/snapshots/6d221c1d-0200-461e-8d20-24b4776b9ddb","rel": "bookmark"}],"created_at": "2015-09-07T11:50:39.756808","description": "Here is a snapshot of share Share1","share_proto": "NFS","share_size": 1,"id": "6d221c1d-0200-461e-8d20-24b4776b9ddb","size": 1}}

