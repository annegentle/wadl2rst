=============================================================================
Show Profile Type Details -  OpenStack Compute API v2.1
=============================================================================

Show Profile Type Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_profile_type_details_v1_profile-types_profile_type_.rst#request>`__
`Response <GET_show_profile_type_details_v1_profile-types_profile_type_.rst#response>`__

.. code-block:: javascript

    GET /v1/profile-types/{profile_type}

Shows details for a profile type.



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
|{profile_type}            |xsd:string               |The name of the profile  |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Profile Type Details: JSON request**


.. code::

    {"profile_type": {"name": "os.heat.stack","schema": {"context": {"default": {},"description": "A dictionary for specifying the customized context for stack operations","required": false,"type": "Map"},"disable_rollback": {"default": true,"description": "A boolean specifying whether a stack operation can be rolled back.","required": false,"type": "Boolean"},"environment": {"default": {},"description": "A map that specifies the environment used for stack operations.","required": false,"type": "Map"},"files": {"default": {},"description": "Contents of files referenced by the template, if any.","required": false,"type": "Map"},"parameters": {"default": {},"description": "Parameters to be passed to Heat for stack operations.","required": false,"type": "Map"},"template": {"description": "Heat stack template.","required": true,"type": "Map"},"timeout": {"description": "A integer that specifies the number of minutes that a stack operation times out.","required": false,"type": "Integer"}}}}

