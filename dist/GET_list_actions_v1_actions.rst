=============================================================================
List Actions -  OpenStack Compute API v2.1
=============================================================================

List Actions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_actions_v1_actions.rst#request>`__
`Response <GET_list_actions_v1_actions.rst#response>`__

.. code-block:: javascript

    GET /v1/actions

Lists all actions.



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
|name                     |xsd:string *(Required)* |Filters the response by an |
|                         |                        |action name. Use this      |
|                         |                        |filter multiple times to   |
|                         |                        |filter by multiple names.  |
+-------------------------+------------------------+---------------------------+
|target                   |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the targeted object ID     |
|                         |                        |that is associated with an |
|                         |                        |action. An object can be a |
|                         |                        |cluster, a node, and so    |
|                         |                        |on. Use this filter        |
|                         |                        |multiple times to filter   |
|                         |                        |by multiple targets.       |
+-------------------------+------------------------+---------------------------+
|action                   |xsd:string *(Required)* |Filters the response by an |
|                         |                        |action name. Use this      |
|                         |                        |filter multiple times to   |
|                         |                        |filter by multiple names.  |
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^





**Example List Actions: JSON request**


.. code::

    {"actions": [{"action": "NODE_CREATE","cause": "RPC Request","created_at": "2015-12-04T04:54:41","depended_by": [],"depends_on": [],"end_time": 1425550000.0,"id": "2366d440-c73e-4961-9254-6d1c3af7c167","inputs": {},"interval": -1,"name": "node_create_0df0931b","outputs": {},"owner": null,"start_time": 1425550000.0,"status": "SUCCEEDED","status_reason": "Action completed successfully.","target": "0df0931b-e251-4f2e-8719-4ebfda3627ba","timeout": 3600,"updated_at": null},{"action": "NODE_DELETE","cause": "RPC Request","created_at": "2015-11-04T05:21:41","depended_by": [],"depends_on": [],"end_time": 1425550000.0,"id": "edce3528-864f-41fb-8759-f4707925cc09","inputs": {},"interval": -1,"name": "node_delete_f0de9b9c","outputs": {},"owner": null,"start_time": 1425550000.0,"status": "SUCCEEDED","status_reason": "Action completed successfully.","target": "f0de9b9c-6d48-4a46-af21-2ca8607777fe","timeout": 3600,"updated_at": null}]}

