=============================================================================
Remove Ipsec Connection -  OpenStack Compute API v2.1
=============================================================================

Remove Ipsec Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_remove_ipsec_connection_v2.0_vpn_ipsec-site-connections_connection_id_.rst#request>`__
`Response <DELETE_remove_ipsec_connection_v2.0_vpn_ipsec-site-connections_connection_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v2.0/vpn/ipsec-site-connections/{connection_id}

Removes an IPSec connection.



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
|{connection_id}           |csapi:UUID               |The UUID of the IPSec    |
|                          |                         |site-to-site connection. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




