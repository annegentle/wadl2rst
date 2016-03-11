=============================================================================
List Events -  OpenStack Compute API v2.1
=============================================================================

List Events
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_events_v1_events.rst#request>`__
`Response <GET_list_events_v1_events.rst#response>`__

.. code-block:: javascript

    GET /v1/events

Lists events.



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
|obj_id                   |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the object ID for an       |
|                         |                        |event. Use this filter     |
|                         |                        |multiple times to filter   |
|                         |                        |by multiple objects.       |
+-------------------------+------------------------+---------------------------+
|obj_type                 |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the type of object         |
|                         |                        |associated with an event.  |
|                         |                        |Use this filter multiple   |
|                         |                        |times to filter by         |
|                         |                        |multiple objects. A valid  |
|                         |                        |value is ``CLUSTER`` or    |
|                         |                        |``NODE``.                  |
+-------------------------+------------------------+---------------------------+
|obj_name                 |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the name of object         |
|                         |                        |associated with an event.  |
|                         |                        |Use this filter multiple   |
|                         |                        |times to filter by         |
|                         |                        |multiple objects.          |
+-------------------------+------------------------+---------------------------+
|cluster_id               |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the cluster ID associated  |
|                         |                        |with an event. Use this    |
|                         |                        |filter multiple times to   |
|                         |                        |filter by multiple         |
|                         |                        |clusters.                  |
+-------------------------+------------------------+---------------------------+
|action                   |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the action name associated |
|                         |                        |with an event. Use this    |
|                         |                        |filter multiple times to   |
|                         |                        |filter by multiple actions.|
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^





**Example List Events: JSON request**


.. code::

    {"events": [{"action": "create","cluster_id": null,"id": "2d255b9c-8f36-41a2-a137-c0175ccc29c3","level": "20","obj_id": "0df0931b-e251-4f2e-8719-4ebfda3627ba","obj_name": "node009","obj_type": "NODE","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","status": "CREATING","status_reason": "Initializing","timestamp": "2015-03-05T08:53:15","user": "a21ded6060534d99840658a777c2af5a"}]}

