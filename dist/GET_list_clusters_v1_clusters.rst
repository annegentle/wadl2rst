=============================================================================
List Clusters -  OpenStack Compute API v2.1
=============================================================================

List Clusters
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_clusters_v1_clusters.rst#request>`__
`Response <GET_list_clusters_v1_clusters.rst#response>`__

.. code-block:: javascript

    GET /v1/clusters

Lists clusters.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^




This table shows the query parameters for the request:

+-------------------------+------------------------+---------------------------+
|Name                     |Type                    |Description                |
+=========================+========================+===========================+
|limit                    |xsd:int *(Required)*    |Requests a page size of    |
|                         |                        |items. Returns a number of |
|                         |                        |items up to a limit value. |
|                         |                        |Use the ``limit``          |
|                         |                        |parameter to make an       |
|                         |                        |initial limited request    |
|                         |                        |and use the ID of the last-|
|                         |                        |seen item from the         |
|                         |                        |response as the ``marker`` |
|                         |                        |parameter value in a       |
|                         |                        |subsequent limited request.|
+-------------------------+------------------------+---------------------------+
|marker                   |xsd:string *(Required)* |The ID of the last-seen    |
|                         |                        |item. Use the ``limit``    |
|                         |                        |parameter to make an       |
|                         |                        |initial limited request    |
|                         |                        |and use the ID of the last-|
|                         |                        |seen item from the         |
|                         |                        |response as the ``marker`` |
|                         |                        |parameter value in a       |
|                         |                        |subsequent limited request.|
+-------------------------+------------------------+---------------------------+
|sort                     |xsd:string *(Required)* |Sorts the response by one  |
|                         |                        |or more attribute and      |
|                         |                        |optional sort direction    |
|                         |                        |combinations. A valid      |
|                         |                        |direction is ``asc``       |
|                         |                        |(ascending) or ``desc``    |
|                         |                        |(descending). Default      |
|                         |                        |direction is ``asc``       |
|                         |                        |(ascending). Specify the   |
|                         |                        |list as < key > [: <       |
|                         |                        |direction > ]. For         |
|                         |                        |example, the following     |
|                         |                        |query parameters in the    |
|                         |                        |URI sort the objects in    |
|                         |                        |the response by ``name``   |
|                         |                        |in ascending order and     |
|                         |                        |then by ``status`` in      |
|                         |                        |descending order: GET      |
|                         |                        |/v2/images?sort=name:asc,  |
|                         |                        |status:descThe following   |
|                         |                        |query parameters in the    |
|                         |                        |URI sort the objects in    |
|                         |                        |the response by ``name``   |
|                         |                        |in descending order and    |
|                         |                        |then by ``status`` in      |
|                         |                        |ascending order. GET       |
|                         |                        |/v2/images?sort=name:desc, |
|                         |                        |status                     |
+-------------------------+------------------------+---------------------------+
|global_project           |xsd:boolean *(Required)*|Indicates whether to       |
|                         |                        |include objects for all    |
|                         |                        |projects or objects for    |
|                         |                        |the current project in the |
|                         |                        |response. If you are an    |
|                         |                        |administrative user and    |
|                         |                        |you set this value to      |
|                         |                        |``True``, the call returns |
|                         |                        |all objects from all       |
|                         |                        |projects. Default is       |
|                         |                        |``False``, which returns   |
|                         |                        |only objects in the        |
|                         |                        |current project.           |
+-------------------------+------------------------+---------------------------+
|name                     |xsd:string *(Required)* |Filters the response by a  |
|                         |                        |cluster name. Use this     |
|                         |                        |filter multiple times to   |
|                         |                        |filter by multiple names.  |
+-------------------------+------------------------+---------------------------+
|status                   |xsd:string *(Required)* |Filters the response by a  |
|                         |                        |cluster status. Use this   |
|                         |                        |filter multiple times to   |
|                         |                        |filter by multiple         |
|                         |                        |statuses.                  |
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|clusters                  |xsd:list *(Required)*    |List of cluster records. |
|                          |                         |Each record contains     |
|                          |                         |fields such as           |
|                          |                         |``created_at``, ``id``,  |
|                          |                         |``name``,                |
|                          |                         |``profile_id``,          |
|                          |                         |``size``, ``nodes``,     |
|                          |                         |``status``,              |
|                          |                         |``status_reason``, and   |
|                          |                         |so on.                   |
+--------------------------+-------------------------+-------------------------+





**Example List Clusters: JSON request**


.. code::

    {"clusters": [{"created_at": "2015-02-10T14:26:14","data": {},"desired_capacity": 4,"domain": null,"id": "7d85f602-a948-4a30-afd4-e84f47471c15","init_at": "2015-02-10T14:26:11","max_size": -1,"metadata": {},"min_size": 0,"name": "cluster1","nodes": ["b07c57c8-7ab2-47bf-bdf8-e894c0c601b9","ecc23d3e-bb68-48f8-8260-c9cf6bcb6e61","da1e9c87-e584-4626-a120-022da5062dac"],"policies": [],"profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","status": "ACTIVE","status_reason": "Cluster scale-in succeeded","timeout": 3600,"updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}]}

