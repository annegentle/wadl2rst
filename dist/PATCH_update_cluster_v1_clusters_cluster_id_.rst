=============================================================================
Update Cluster -  OpenStack Compute API v2.1
=============================================================================

Update Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PATCH_update_cluster_v1_clusters_cluster_id_.rst#request>`__
`Response <PATCH_update_cluster_v1_clusters_cluster_id_.rst#response>`__

.. code-block:: javascript

    PATCH /v1/clusters/{cluster_id}

Updates a cluster.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|cluster                   |xsd:dict *(Required)*    |A map of cluster details.|
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name of the cluster. |
+--------------------------+-------------------------+-------------------------+
|parent                    |csapi:UUID *(Required)*  |The UUID of the parent   |
|                          |                         |cluster if the cluster   |
|                          |                         |is a nested cluster.     |
+--------------------------+-------------------------+-------------------------+
|profile_id                |xsd:string *(Required)*  |The ID or name of the    |
|                          |                         |profile for the cluster. |
+--------------------------+-------------------------+-------------------------+
|timeout                   |xsd:int *(Required)*     |The timeout value, in    |
|                          |                         |minutes, for cluster     |
|                          |                         |creation. Default is 60. |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:dict *(Required)*    |A set of key and value   |
|                          |                         |pairs to associate with  |
|                          |                         |the cluster.             |
+--------------------------+-------------------------+-------------------------+





**Example Update Cluster: JSON request**


.. code::

    {"cluster": {"metadata": null,"name": null,"profile_id": null,"timeout": "30"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|cluster                   |xsd:dict *(Required)*    |A map with the ``id``,   |
|                          |                         |``name``, ``status``,    |
|                          |                         |and other fields for the |
|                          |                         |cluster.                 |
+--------------------------+-------------------------+-------------------------+





**Example Update Cluster: JSON request**


.. code::

    {"cluster": {"created_at": "2015-02-11T15:13:20","data": {},"desired_capacity": 0,"domain": null,"id": "45edadcb-c73b-4920-87e1-518b2f29f54b","init_at": "2015-02-10T14:26:10","max_size": -1,"metadata": {},"min_size": 0,"name": "test_cluster","nodes": [],"policies": [],"profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","status": "INIT","status_reason": "Initializing","timeout": 3600,"updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

