=============================================================================
Show Task Details -  OpenStack Image API v2
=============================================================================

Show Task Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_task_details_v2_tasks_task_id_.rst#request>`__
`Response <GET_show_task_details_v2_tasks_task_id_.rst#response>`__

.. code-block:: javascript

    GET /v2/tasks/{task_id}

Shows details for a task.



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
|{task_id}                 |csapi:UUID               |The UUID of the task.    |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|task_id                   |csapi:UUID *(Required)*  |The UUID of the task.    |
+--------------------------+-------------------------+-------------------------+





Response
^^^^^^^^^^^^^^^^^^





**Example Show Task Details: JSON request**


.. code::

    {
        "id": "e7e59ff6-fa2e-4075-87d3-1a1398a07dc3",
        "type": "import",
        "status": "pending"
    }
    

