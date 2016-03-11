=============================================================================
List Profiles -  OpenStack Compute API v2.1
=============================================================================

List Profiles
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_profiles_v1_profiles.rst#request>`__
`Response <GET_list_profiles_v1_profiles.rst#response>`__

.. code-block:: javascript

    GET /v1/profiles

Lists all profiles.



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
|                         |                        |the name of a profile.     |
+-------------------------+------------------------+---------------------------+
|type                     |xsd:string *(Required)* |Filters the response by    |
|                         |                        |the type of a profile.     |
+-------------------------+------------------------+---------------------------+
|metadata                 |xsd:dict *(Required)*   |Filters the response by a  |
|                         |                        |metadata key and value     |
|                         |                        |pair.                      |
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|profiles                  |xsd:list *(Required)*    |Profile records. Each    |
|                          |                         |record contains the      |
|                          |                         |``id``, ``name``,        |
|                          |                         |``type``, ``spec``,      |
|                          |                         |``metadata``, and other  |
|                          |                         |fields.                  |
+--------------------------+-------------------------+-------------------------+





**Example List Profiles: JSON request**


.. code::

    {"profiles": [{"created_at": "2015-02-10T11:46:33.000000","domain": null,"id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","metadata": {},"name": "mystack","project": "42d9e9663331431f97b75e25136307ff","spec": {"properties": {"disable_rollback": false,"environment": {"resource_registry": {"os.heat.server": "OS::Heat::Server"}},"files": {"file:///opt/stack/senlin/examples/profiles/test_script.sh": "#!/bin/bash\n\necho \"this is a test script file\"\n"},"name": "random_string_stack","parameters": {},"rollback": false,"template": {"heat_template_version": "2014-10-16","outputs": {"result": {"value": {"get_attr": ["random","value"]}}},"parameters": {"file": {"default": {"get_file": "file:///opt/stack/senlin/examples/profiles/test_script.sh"},"type": "string"}},"resources": {"random": {"properties": {"length": 64},"type": "OS::Heat::RandomString"}}},"timeout": 60},"type": "os.heat.stack","version": "1.0"},"type": "os.heat.stack-1.0","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}]}

