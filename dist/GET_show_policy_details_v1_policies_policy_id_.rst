=============================================================================
Show Policy Details -  OpenStack Compute API v2.1
=============================================================================

Show Policy Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_policy_details_v1_policies_policy_id_.rst#request>`__
`Response <GET_show_policy_details_v1_policies_policy_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/policies/{policy_id}

Shows details for a policy.



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








Response
^^^^^^^^^^^^^^^^^^





**Example Show Policy Details: JSON request**


.. code::

    {"policy": {"created_at": "2015-03-02T07:40:31","data": {},"domain": null,"id": "02f62195-2198-4797-b0a9-877632208527","name": "sp001","project": "42d9e9663331431f97b75e25136307ff","spec": {"properties": {"adjustment": {"best_effort": true,"min_step": 1,"number": 1,"type": "CHANGE_IN_CAPACITY"},"event": "CLUSTER_SCALE_IN"},"type": "senlin.policy.scaling","version": "1.0"},"type": "senlin.policy.scaling-1.0","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

