=============================================================================
List Tasks -  OpenStack Image API v2
=============================================================================

List Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_tasks_v2_tasks.rst#request>`__
`Response <GET_list_tasks_v2_tasks.rst#response>`__

.. code-block:: javascript

    GET /v2/tasks

Lists tasks.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^




This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|sort_dir                  |xsd:string *(Required)*  |Sorts the response by a  |
|                          |                         |set of one or more sort  |
|                          |                         |direction and attribute  |
|                          |                         |( ``sort_key`` )         |
|                          |                         |combinations. A valid    |
|                          |                         |value for the sort       |
|                          |                         |direction is ``asc``     |
|                          |                         |(ascending) or ``desc``  |
|                          |                         |(descending). If you     |
|                          |                         |omit the sort direction  |
|                          |                         |in a set, the default is |
|                          |                         |``desc``.                |
+--------------------------+-------------------------+-------------------------+
|sort_key                  |xsd:string *(Required)*  |Sorts the response by an |
|                          |                         |attribute, such as       |
|                          |                         |``name``, ``id``, or     |
|                          |                         |``updated_at``. Default  |
|                          |                         |is ``created_at``. The   |
|                          |                         |API uses the natural     |
|                          |                         |sorting direction of the |
|                          |                         |``sort_key`` image       |
|                          |                         |attribute.               |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |Filters the response by  |
|                          |                         |a task type. A valid     |
|                          |                         |value is ``import``.     |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |Filters the response by  |
|                          |                         |a task status. A valid   |
|                          |                         |value is ``pending``,    |
|                          |                         |``processing``,          |
|                          |                         |``success``, or          |
|                          |                         |``failure``.             |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|tasks                     |xsd:list *(Required)*    |A list of ``task``       |
|                          |                         |objects.                 |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the task.    |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |The type of task         |
|                          |                         |represented by this      |
|                          |                         |content.                 |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |The current status of    |
|                          |                         |this task. The value can |
|                          |                         |be "pending",            |
|                          |                         |"processing", "success"  |
|                          |                         |or "failure".            |
+--------------------------+-------------------------+-------------------------+





**Example List Tasks: JSON request**


.. code::

    {
        "tasks": [
            {
                "id": "cbc36478b0bd8e67e89469c7749d4127",
                "type": "import",
                "status": "pending"
            },
            {
                "id": "bbc36578b0bd8e67e89469c7749d4126",
                "type": "import",
                "status": "processing"
            }
        ]
    }
    

