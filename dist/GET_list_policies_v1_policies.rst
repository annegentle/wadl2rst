=============================================================================
List Policies -  OpenStack Compute API v2.1
=============================================================================

List Policies
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_policies_v1_policies.rst#request>`__
`Response <GET_list_policies_v1_policies.rst#response>`__

.. code-block:: javascript

    GET /v1/policies

Lists all policies.



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
|name                     |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the name of a policy.      |
+-------------------------+------------------------+---------------------------+
|type                     |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the type of a policy.      |
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|policies                  |xsd:list *(Required)*    |List of policy records.  |
|                          |                         |Each record contains     |
|                          |                         |fields such as ``id``,   |
|                          |                         |``name``, ``type``,      |
|                          |                         |``spec``, and so on.     |
+--------------------------+-------------------------+-------------------------+





**Example List Policies: JSON request**


.. code::

    {"policies": [{"created_at": "2015-02-15T08:33:13.000000","data": {},"domain": null,"id": "7192d8df-73be-4e98-ab99-1cf6d5066729","name": "test_policy_1","project": "42d9e9663331431f97b75e25136307ff","spec": {"description": "A test policy","properties": {"criteria": "OLDEST_FIRST","destroy_after_deletion": true,"grace_period": 60,"reduce_desired_capacity": false},"type": "senlin.policy.deletion","version": "1.0"},"type": "senlin.policy.deletion-1.0","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}]}

