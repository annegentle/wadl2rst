=============================================================================
Delete Policy -  OpenStack Compute API v2.1
=============================================================================

Delete Policy
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_policy_v1_policies_policy_id_.rst#request>`__
`Response <DELETE_delete_policy_v1_policies_policy_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v1/policies/{policy_id}

Deletes a policy.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
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




