=============================================================================
Delete Cluster -  OpenStack Compute API v2.1
=============================================================================

Delete Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_cluster_v1_clusters_cluster_id_.rst#request>`__
`Response <DELETE_delete_cluster_v1_clusters_cluster_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v1/clusters/{cluster_id}

Deletes a cluster.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{cluster_id}              |csapi:UUID *(Required)*  |The UUID of the cluster. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




