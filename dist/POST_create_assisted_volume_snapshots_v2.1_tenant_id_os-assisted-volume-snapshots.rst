=============================================================================
Create Assisted Volume Snapshots -  OpenStack Compute API v2.1
=============================================================================

Create Assisted Volume Snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_assisted_volume_snapshots_v2.1_tenant_id_os-assisted-volume-snapshots.rst#request>`__
`Response <POST_create_assisted_volume_snapshots_v2.1_tenant_id_os-assisted-volume-snapshots.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-assisted-volume-snapshots

Creates an assisted volume snapshot.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|volume_id                 |xsd:string *(Required)*  |The source volume ID.    |
+--------------------------+-------------------------+-------------------------+
|create_info               |xsd:dict *(Required)*    |Information for snapshot |
|                          |                         |creation.                |
+--------------------------+-------------------------+-------------------------+
|snapshot_id               |xsd:string *(Required)*  |The snapshot ID.         |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |The snapshot type. A     |
|                          |                         |valid value is ``qcow2``.|
+--------------------------+-------------------------+-------------------------+
|new_file                  |xsd:string *(Required)*  |The name of the qcow2    |
|                          |                         |file that Block Storage  |
|                          |                         |creates, which becomes   |
|                          |                         |the active image for the |
|                          |                         |VM.                      |
+--------------------------+-------------------------+-------------------------+





**Example Create Assisted Volume Snapshots: JSON request**


.. code::

    {
        "snapshot": {
            "volume_id": "521752a6-acf6-4b2d-bc7a-119f9148cd8c",
            "create_info": {
                "snapshot_id": "421752a6-acf6-4b2d-bc7a-119f9148cd8c",
                "type": "qcow2",
                "new_file": "new_file_name"
            }
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |xsd:string *(Required)*  |The snapshot ID.         |
+--------------------------+-------------------------+-------------------------+
|volume_id                 |xsd:string *(Required)*  |The source volume ID.    |
+--------------------------+-------------------------+-------------------------+





**Example Create Assisted Volume Snapshots: JSON request**


.. code::

    {
        "snapshot": {
            "id": 100,
            "volumeId": "521752a6-acf6-4b2d-bc7a-119f9148cd8c"
        }
    }
    

