=============================================================================
Delete A Cluster -  OpenStack Compute API v2.1
=============================================================================

Delete A Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_a_cluster_v1.1_tenant_id_clusters_cluster_id_.rst#request>`__
`Response <DELETE_delete_a_cluster_v1.1_tenant_id_clusters_cluster_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v1.1/{tenant_id}/clusters/{cluster_id}

Deletes a cluster.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{cluster_id}              |csapi:UUID               |The ID of the cluster    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




