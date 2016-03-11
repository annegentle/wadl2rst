=============================================================================
Create Profile -  OpenStack Compute API v2.1
=============================================================================

Create Profile
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_profile_v1_profiles.rst#request>`__
`Response <POST_create_profile_v1_profiles.rst#response>`__

.. code-block:: javascript

    POST /v1/profiles

Creates a profile.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|profile                   |xsd:dict *(Required)*    |A map with details for   |
|                          |                         |the profile.             |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name for the profile.|
+--------------------------+-------------------------+-------------------------+
|spec                      |xsd:string *(Required)*  |Detailed specification   |
|                          |                         |based on the chosen      |
|                          |                         |profile type.            |
+--------------------------+-------------------------+-------------------------+
|metadata                  |xsd:list *(Required)*    |A list of key and value  |
|                          |                         |pairs to associate with  |
|                          |                         |the profile.             |
+--------------------------+-------------------------+-------------------------+





**Example Create Profile: JSON request**


.. code::

    {"profile": {"metadata": {},"name": "test_prof1","spec": {"properties": {"disable_rollback": false,"environment": {"resource_registry": {"os.heat.server": "OS::Heat::Server"}},"files": {"file:///usr/test_script.sh": "#!/bin/bash\n\necho \"this is a test script file\"\n"},"parameters": {},"template": {"heat_template_version": "2014-10-16","outputs": {"result": {"value": {"get_attr": ["random","value"]}}},"parameters": {"file": {"default": {"get_file": "file:///usr/test_script.sh"},"type": "string"}},"resources": {"random": {"properties": {"length": 64},"type": "OS::Heat::RandomString"}}},"timeout": 60},"type": "os.heat.stack","version": "1.0"}}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|profile                   |xsd:dict *(Required)*    |A dictionary with        |
|                          |                         |profile details. Profile |
|                          |                         |create response``id`` An |
|                          |                         |unique ID for the        |
|                          |                         |profile. ``name`` Name   |
|                          |                         |for the profile.         |
|                          |                         |``type`` Name of policy  |
|                          |                         |type referenced by the   |
|                          |                         |profile. ``spec``        |
|                          |                         |Detailed specification   |
|                          |                         |based on the profile     |
|                          |                         |type. ``metadata`` A     |
|                          |                         |list of key and value    |
|                          |                         |pairs that are attached  |
|                          |                         |to the profile.          |
|                          |                         |``created_at`` The UTC   |
|                          |                         |date and time stamp when |
|                          |                         |the profile was created. |
|                          |                         |``updated_at`` The UTC   |
|                          |                         |date and time stamp when |
|                          |                         |the profile was updated. |
|                          |                         |``domain`` The ID of the |
|                          |                         |domain to which the      |
|                          |                         |profile belongs.         |
|                          |                         |``project`` The ID of    |
|                          |                         |the project to which the |
|                          |                         |profile belongs.         |
|                          |                         |``user`` The ID of the   |
|                          |                         |user who created the     |
|                          |                         |profile.                 |
+--------------------------+-------------------------+-------------------------+





**Example Create Profile: JSON request**


.. code::

    {"profile": {"created_at": "2015-03-01T14:28:25","domain": null,"id": "7fa885cd-fa39-4531-a42d-780af95c84a4","metadata": {},"name": "test_prof1","project": "42d9e9663331431f97b75e25136307ff","spec": {"properties": {"disable_rollback": false,"environment": {"resource_registry": {"os.heat.server": "OS::Heat::Server"}},"files": {"file:///opt/stack/senlin/examples/profiles/test_script.sh": "#!/bin/bash\n\necho \"this is a test script file\"\n"},"parameters": {},"template": {"heat_template_version": "2014-10-16","outputs": {"result": {"value": {"get_attr": ["random","value"]}}},"parameters": {"file": {"default": {"get_file": "file:///opt/stack/senlin/examples/profiles/test_script.sh"},"type": "string"}},"resources": {"random": {"properties": {"length": 64},"type": "OS::Heat::RandomString"}}},"timeout": 60},"type": "os.heat.stack","version": "1.0"},"type": "os.heat.stack-1.0","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

