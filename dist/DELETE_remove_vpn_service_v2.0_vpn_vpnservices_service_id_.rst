=============================================================================
Remove Vpn Service -  OpenStack Compute API v2.1
=============================================================================

Remove Vpn Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_remove_vpn_service_v2.0_vpn_vpnservices_service_id_.rst#request>`__
`Response <DELETE_remove_vpn_service_v2.0_vpn_vpnservices_service_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/vpn/vpnservices/{service_id}

Removes a VPN service.

If the service has connections, the request is rejected.



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
|{service_id}              |csapi:UUID               |The UUID of the VPN      |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




