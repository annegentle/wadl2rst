=============================================================================
Update Policy -  OpenStack Compute API v2.1
=============================================================================

Update Policy
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PATCH_update_policy_v1_policies_policy_id_.rst#request>`__
`Response <PATCH_update_policy_v1_policies_policy_id_.rst#response>`__

.. code-block:: javascript

    PATCH /v1/policies/{policy_id}

Updates a policy.



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
|{policy_id}               |csapi:UUID *(Required)*  |The UUID of the policy.  |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|policy                    |xsd:dict *(Required)*    |A map with a set of key  |
|                          |                         |and value pairs that     |
|                          |                         |specify the details of   |
|                          |                         |the policy: Policy       |
|                          |                         |body``name`` Name for    |
|                          |                         |the policy, if specified.|
+--------------------------+-------------------------+-------------------------+





**Example Update Policy: JSON request**


.. code::

    {"policy": {"name": "new_name"}}


Response
^^^^^^^^^^^^^^^^^^





**Example Update Policy: JSON request**


.. code::

    {"policy": {"created_at": "2015-10-14T09:14:53","data": {},"domain": null,"id": "ac5415bd-f522-4160-8be0-f8853e4bc332","name": "dp01","project": "42d9e9663331431f97b75e25136307ff","spec": {"description": "A policy for node deletion.","properties": {"criteria": "OLDEST_FIRST","destroy_after_deletion": true,"grace_period": 60,"reduce_desired_capacity": false},"type": "senlin.policy.deletion","version": "1.0"},"type": "senlin.policy.deletion-1.0","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

