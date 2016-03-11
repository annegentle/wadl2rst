=============================================================================
Show Profile Details -  OpenStack Compute API v2.1
=============================================================================

Show Profile Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_profile_details_v1_profiles_profile_id_.rst#request>`__
`Response <GET_show_profile_details_v1_profiles_profile_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/profiles/{profile_id}

Shows details for a profile.



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
|{profile_id}              |csapi:UUID *(Required)*  |The UUID of the profile. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Profile Details: JSON request**


.. code::

    {"profile": {"created_at": "2015-03-01T14:28:25","domain": null,"id": "7fa885cd-fa39-4531-a42d-780af95c84a4","metadata": {},"name": "test_prof1","project": "42d9e9663331431f97b75e25136307ff","spec": {"disable_rollback": false,"environment": {"resource_registry": {"os.heat.server": "OS::Heat::Server"}},"files": {"file:///opt/stack/senlin/examples/profiles/test_script.sh": "#!/bin/bash\n\necho \"this is a test script file\"\n"},"parameters": {},"template": {"heat_template_version": "2014-10-16","outputs": {"result": {"value": {"get_attr": ["random","value"]}}},"parameters": {"file": {"default": {"get_file": "file:///opt/stack/senlin/examples/profiles/test_script.sh"},"type": "string"}},"resources": {"random": {"properties": {"length": 64},"type": "OS::Heat::RandomString"}},"timeout": 60},"type": "os.heat.stack","version": "1.0"},"type": "os.heat.stack-1.0","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

