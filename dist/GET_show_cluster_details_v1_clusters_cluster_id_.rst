=============================================================================
Show Cluster Details -  OpenStack Compute API v2.1
=============================================================================

Show Cluster Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_cluster_details_v1_clusters_cluster_id_.rst#request>`__
`Response <GET_show_cluster_details_v1_clusters_cluster_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/clusters/{cluster_id}

Shows details for a cluster.



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
|{cluster_id}              |csapi:UUID *(Required)*  |The UUID of the cluster. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Cluster Details: JSON request**


.. code::

    {"cluster": {"created_at": "2015-02-11T15:13:20","data": {},"desired_capacity": 0,"domain": null,"id": "45edadcb-c73b-4920-87e1-518b2f29f54b","init_at": "2015-02-10T14:26:10","max_size": -1,"metadata": {},"min_size": 0,"name": "test_cluster","nodes": [],"policies": [],"profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","status": "ACTIVE","status_reason": "Creation succeeded","timeout": 3600,"updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

