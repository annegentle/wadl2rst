=============================================================================
Remove Ipsec Policy -  OpenStack Compute API v2.1
=============================================================================

Remove Ipsec Policy
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_remove_ipsec_policy_v2.0_vpn_ipsecpolicies_ipsecpolicy_id_.rst#request>`__
`Response <DELETE_remove_ipsec_policy_v2.0_vpn_ipsecpolicies_ipsecpolicy_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}

Removes an IPSec policy.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{ipsecpolicy_id}          |csapi:UUID               |The UUID of the IPSec    |
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




