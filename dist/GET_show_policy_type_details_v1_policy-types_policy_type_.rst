=============================================================================
Show Policy Type Details -  OpenStack Compute API v2.1
=============================================================================

Show Policy Type Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_policy_type_details_v1_policy-types_policy_type_.rst#request>`__
`Response <GET_show_policy_type_details_v1_policy-types_policy_type_.rst#response>`__

.. code-block:: javascript

    GET /v1/policy-types/{policy_type}

Shows details for a policy type.



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
|{policy_type}             |xsd:string *(Required)*  |The name of the policy   |
|                          |                         |type.                    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Policy Type Details: JSON request**


.. code::

    {"policy_type": {"name": "senlin.policy.deletion","schema": {"criteria": {"constraints": [{"constraint": ["OLDEST_FIRST","OLDEST_PROFILE_FRIST","YOUNGEST_FIRST","RANDOM"],"type": "AllowedValues"}],"default": "RANDOM","description": "Criteria used in selecting candidates for deletion","required": false,"type": "String"},"destroy_after_deletion": {"default": true,"description": "Whether a node should be completely destroyed after deletion. Default to True","required": false,"type": "Boolean"},"grace_period": {"default": 0,"description": "Number of seconds before real deletion happens.","required": false,"type": "Integer"},"reduce_desired_capacity": {"default": false,"description": "Whether the desired capacity of the cluster should be reduced along the deletion. Default to False.","required": false,"type": "Boolean"}}}}

