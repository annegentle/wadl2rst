=============================================================================
List Nodes -  OpenStack Compute API v2.1
=============================================================================

List Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_nodes_v1_nodes.rst#request>`__
`Response <GET_list_nodes_v1_nodes.rst#response>`__

.. code-block:: javascript

    GET /v1/nodes

Lists all nodes.



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
|cluster_id               |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the cluster that owns a    |
|                         |                        |node.                      |
+-------------------------+------------------------+---------------------------+
|name                     |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the name of a node.        |
+-------------------------+------------------------+---------------------------+
|status                   |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the status of a node.      |
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|nodes                     |xsd:list *(Required)*    |List of node records.    |
|                          |                         |Each record contains     |
|                          |                         |fields such as ``id``,   |
|                          |                         |``cluster_id``,          |
|                          |                         |``name``,                |
|                          |                         |``physical_id``,         |
|                          |                         |``profile_id``,          |
|                          |                         |``created_at``,          |
|                          |                         |``index``, ``status``,   |
|                          |                         |``status_reason``,       |
|                          |                         |``metadata``,            |
|                          |                         |``updated_at``, and so   |
|                          |                         |on.                      |
+--------------------------+-------------------------+-------------------------+





**Example List Nodes: JSON request**


.. code::

    {"nodes": [{"cluster_id": null,"created_at": "2015-02-27T04:39:21","data": {},"details": {},"domain": null,"id": "573aa1ba-bf45-49fd-907d-6b5d6e6adfd3","index": -1,"init_at": "2015-02-27T04:39:18","metadata": {},"name": "node00a","physical_id": "cc028275-d078-4729-bf3e-154b7359814b","profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","role": null,"status": "ACTIVE","status_reason": "Creation succeeded","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}]}

