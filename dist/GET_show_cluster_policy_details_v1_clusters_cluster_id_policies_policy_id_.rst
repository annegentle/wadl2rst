=============================================================================
Show Cluster Policy Details -  OpenStack Compute API v2.1
=============================================================================

Show Cluster Policy Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_cluster_policy_details_v1_clusters_cluster_id_policies_policy_id_.rst#request>`__
`Response <GET_show_cluster_policy_details_v1_clusters_cluster_id_policies_policy_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/clusters/{cluster_id}/policies/{policy_id}

Shows details for a policy for a cluster.



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
|{policy_id}               |csapi:UUID *(Required)*  |The UUID of the policy.  |
+--------------------------+-------------------------+-------------------------+
|{cluster_id}              |csapi:UUID *(Required)*  |The UUID of the cluster. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Cluster Policy Details: JSON request**


.. code::

    {"cluster_policy": {"cluster_id": "7d85f602-a948-4a30-afd4-e84f47471c15","cluster_name": "cluster4","enabled": true,"id": "06be3a1f-b238-4a96-a737-ceec5714087e","policy_id": "714fe676-a08f-4196-b7af-61d52eeded15","policy_name": "dp01","policy_type": "senlin.policy.deletion-1.0"}}

