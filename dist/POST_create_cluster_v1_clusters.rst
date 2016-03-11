=============================================================================
Create Cluster -  OpenStack Compute API v2.1
=============================================================================

Create Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_cluster_v1_clusters.rst#request>`__
`Response <POST_create_cluster_v1_clusters.rst#response>`__

.. code-block:: javascript

    POST /v1/clusters

Creates a cluster.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






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
|desired_capacity          |xsd:int *(Required)*     |The capacity, or initial |
|                          |                         |size, of the cluster.    |
|                          |                         |Default is 0.            |
+--------------------------+-------------------------+-------------------------+
|min_size                  |xsd:int *(Required)*     |The minimum size of the  |
|                          |                         |cluster. Default is 0.   |
+--------------------------+-------------------------+-------------------------+
|max_size                  |xsd:int *(Required)*     |The maximum size of the  |
|                          |                         |cluster. Default is ``-  |
|                          |                         |1``, which indicates     |
|                          |                         |that no upper limit      |
|                          |                         |exists for the cluster   |
|                          |                         |size.                    |
+--------------------------+-------------------------+-------------------------+
|timeout                   |xsd:int *(Required)*     |The timeout value, in    |
|                          |                         |minutes, for cluster     |
|                          |                         |creation. Default is 60. |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:dict *(Required)*    |A set of key and value   |
|                          |                         |pairs to associate with  |
|                          |                         |the cluster.             |
+--------------------------+-------------------------+-------------------------+





**Example Create Cluster: JSON request**


.. code::

    {"cluster": {"desired_capacity": 0,"max_size": -1,"metadata": {},"min_size": 0,"name": "test_cluster","profile_id": "mystack","timeout": null}}


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





**Example Create Cluster: JSON request**


.. code::

    {"cluster": {"action": "bbf4558b-9fa3-482a-93c2-a4aa5cc85317","created_at": null,"data": {},"desired_capacity": 4,"domain": null,"id": "45edadcb-c73b-4920-87e1-518b2f29f54b","init_at": "2015-02-10T14:16:10","max_size": -1,"metadata": {},"min_size": 0,"name": "test_cluster","nodes": [],"policies": [],"profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","status": "INIT","status_reason": "Initializing","timeout": 3600,"updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

