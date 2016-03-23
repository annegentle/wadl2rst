=============================================================================
Create Task -  OpenStack Image API v2
=============================================================================

Create Task
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_task_v2_tasks.rst#request>`__
`Response <POST_create_task_v2_tasks.rst#response>`__

.. code-block:: javascript

    POST /v2/tasks

Creates a task.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |The type of the task.    |
|                          |                         |Task source information. |
|                          |                         |The location useded for  |
|                          |                         |importing the task. The  |
|                          |                         |format of the image. The |
|                          |                         |properties of the image. |
|                          |                         |The disk format of the   |
|                          |                         |image. The container     |
|                          |                         |format of the image.     |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









**Example Create Task: JSON request**


.. code::

    {
        "type": "import",
        "input": {
            "import_from": "http://example.com",
            "import_from_format": "qcow2",
            "image_properties": {
                "disk_format": "vhd",
                "container_format": "ovf"
            }
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|type                      |xsd:string *(Required)*  |The type of the task.    |
+--------------------------+-------------------------+-------------------------+
|input                     |xsd:list *(Required)*    |Task source information. |
+--------------------------+-------------------------+-------------------------+
|import_from               |xsd:string *(Required)*  |The location useded for  |
|                          |                         |importing the task.      |
+--------------------------+-------------------------+-------------------------+
|import_from_format        |xsd:string *(Required)*  |The format of the image. |
+--------------------------+-------------------------+-------------------------+
|image_properties          |xsd:list *(Required)*    |The properties of the    |
|                          |                         |image.                   |
+--------------------------+-------------------------+-------------------------+
|disk_format               |xsd:string *(Required)*  |The disk format of the   |
|                          |                         |image.                   |
+--------------------------+-------------------------+-------------------------+
|container_format          |xsd:string *(Required)*  |The container format of  |
|                          |                         |the image.               |
+--------------------------+-------------------------+-------------------------+




