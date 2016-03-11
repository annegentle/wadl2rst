=============================================================================
Remove Vpn Endpoint Group -  OpenStack Compute API v2.1
=============================================================================

Remove Vpn Endpoint Group
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_remove_vpn_endpoint_group_v2.0_vpn_endpoint-groups_endpoint_group_id_.rst#request>`__
`Response <DELETE_remove_vpn_endpoint_group_v2.0_vpn_endpoint-groups_endpoint_group_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/vpn/endpoint-groups/{endpoint_group_id}

Removes a VPN endpoint group.



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
|{endpoint_group_id}       |csapi:UUID               |The UUID of the VPN      |
|                          |                         |endpoint group.          |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




