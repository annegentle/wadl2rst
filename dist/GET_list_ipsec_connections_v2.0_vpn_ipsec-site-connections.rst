=============================================================================
List Ipsec Connections -  OpenStack Compute API v2.1
=============================================================================

List Ipsec Connections
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_ipsec_connections_v2.0_vpn_ipsec-site-connections.rst#request>`__
`Response <GET_list_ipsec_connections_v2.0_vpn_ipsec-site-connections.rst#response>`__

.. code-block:: javascript

    GET /v2.0/vpn/ipsec-site-connections

Lists all IPSec connections.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |csapi:UUID *(Required)*  |The UUID for the IPSec   |
|                          |                         |connection.              |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |Owner of the IPSec       |
|                          |                         |connection. Only         |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the IPSec connection.    |
|                          |                         |Does not have to be      |
|                          |                         |unique.                  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the      |
|                          |                         |IPSec connection.        |
+--------------------------+-------------------------+-------------------------+
|peer_address              |xsd:string *(Required)*  |The peer gateway public  |
|                          |                         |IPv4 address, IPv6       |
|                          |                         |address, or FQDN.        |
+--------------------------+-------------------------+-------------------------+
|peer_id                   |xsd:string *(Required)*  |The peer router identity |
|                          |                         |for authentication. Can  |
|                          |                         |be an IPv4 address, IPv6 |
|                          |                         |address, e-mail address, |
|                          |                         |key ID, or FQDN.         |
|                          |                         |Typically, this value    |
|                          |                         |matches the              |
|                          |                         |``peer_address`` value.  |
+--------------------------+-------------------------+-------------------------+
|local_ep_group_id         |csapi:UUID *(Required)*  |The UUID for the         |
|                          |                         |endpoint group that      |
|                          |                         |contains private subnets |
|                          |                         |for the local side of    |
|                          |                         |the connection. This     |
|                          |                         |value is present with    |
|                          |                         |the ``peer_ep_group_id`` |
|                          |                         |parameter unless in      |
|                          |                         |backward-compatible      |
|                          |                         |mode, where              |
|                          |                         |``peer_cidrs`` is shown. |
+--------------------------+-------------------------+-------------------------+
|peer_ep_group_id          |csapi:UUID *(Required)*  |The UUID for the         |
|                          |                         |endpoint group that      |
|                          |                         |contains private CIDRs   |
|                          |                         |in the form <            |
|                          |                         |net_address > / < prefix |
|                          |                         |> for the peer side of   |
|                          |                         |the connection. This     |
|                          |                         |value is present with    |
|                          |                         |the                      |
|                          |                         |``local_ep_group_id``    |
|                          |                         |parameter unless in      |
|                          |                         |backward-compatible      |
|                          |                         |mode, where              |
|                          |                         |``peer_cidrs`` is shown. |
+--------------------------+-------------------------+-------------------------+
|peer_cidrs                |xsd:list *(Required)*    |(Deprecated) Unique list |
|                          |                         |of valid peer private    |
|                          |                         |CIDRs in the form <      |
|                          |                         |net_address > / < prefix |
|                          |                         |>.                       |
+--------------------------+-------------------------+-------------------------+
|route_mode                |xsd:string *(Required)*  |The route mode. A valid  |
|                          |                         |value is ``static``,     |
|                          |                         |which is the default.    |
+--------------------------+-------------------------+-------------------------+
|mtu                       |xsd:int *(Required)*     |The maximum transmission |
|                          |                         |unit (MTU) to address    |
|                          |                         |fragmentation. The       |
|                          |                         |minimum value for IPv4   |
|                          |                         |is 68. The minimum value |
|                          |                         |for IPv6 is 1280.        |
+--------------------------+-------------------------+-------------------------+
|auth_mode                 |xsd:string *(Required)*  |The authentication mode. |
|                          |                         |A valid value is         |
|                          |                         |``psk``, which is the    |
|                          |                         |default.                 |
+--------------------------+-------------------------+-------------------------+
|psk                       |xsd:string *(Required)*  |The pre-shared key. A    |
|                          |                         |valid value is any       |
|                          |                         |string.                  |
+--------------------------+-------------------------+-------------------------+
|initiator                 |xsd:string *(Required)*  |Indicates whether this   |
|                          |                         |VPN can only respond to  |
|                          |                         |connections or both      |
|                          |                         |respond to and initiate  |
|                          |                         |connections. A valid     |
|                          |                         |value is ``response-     |
|                          |                         |only`` or ``bi-          |
|                          |                         |directional``. Default   |
|                          |                         |is ``bi-directional``.   |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the IPSec connection, |
|                          |                         |which is up ( ``true`` ) |
|                          |                         |or down ( ``false`` ).   |
|                          |                         |If down, the connection  |
|                          |                         |does not forward packets.|
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |Indicates whether the    |
|                          |                         |IPSec connection is      |
|                          |                         |currently operational.   |
|                          |                         |Value is ``ACTIVE``,     |
|                          |                         |``DOWN``, ``BUILD``,     |
|                          |                         |``ERROR``,               |
|                          |                         |``PENDING_CREATE``,      |
|                          |                         |``PENDING_UPDATE``, or   |
|                          |                         |``PENDING_DELETE``.      |
+--------------------------+-------------------------+-------------------------+
|ikepolicy_id              |csapi:UUID *(Required)*  |The UUID of the IKE      |
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+
|ipsecpolicy_id            |csapi:UUID *(Required)*  |The UUID of the IPSec    |
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+
|vpnservice_id             |csapi:UUID *(Required)*  |The UUID of the VPN      |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+
|dpd                       |xsd:dict *(Required)*    |A dictionary with dead   |
|                          |                         |peer detection (DPD)     |
|                          |                         |protocol controls.       |
+--------------------------+-------------------------+-------------------------+
|action                    |xsd:string *(Required)*  |The dead peer detection  |
|                          |                         |(DPD) action. A valid    |
|                          |                         |value is ``clear``,      |
|                          |                         |``hold``, ``restart``,   |
|                          |                         |``disabled``, or         |
|                          |                         |``restart-by-peer``.     |
|                          |                         |Default value is         |
|                          |                         |``hold``.                |
+--------------------------+-------------------------+-------------------------+
|interval                  |xsd:int *(Required)*     |The dead peer detection  |
|                          |                         |(DPD) interval, in       |
|                          |                         |seconds. A valid value   |
|                          |                         |is a positive integer.   |
|                          |                         |Default is 30.           |
+--------------------------+-------------------------+-------------------------+
|timeout                   |xsd:int *(Required)*     |The dead peer detection  |
|                          |                         |(DPD) timeout, in        |
|                          |                         |seconds. A valid value   |
|                          |                         |is a positive integer    |
|                          |                         |that is greater than the |
|                          |                         |DPD ``interval`` value.  |
|                          |                         |Default is 120.          |
+--------------------------+-------------------------+-------------------------+





**Example List Ipsec Connections: JSON request**


.. code::

    {"ipsec_site_connections": [{"status": "PENDING CREATE","psk": "secret","initiator": "bi-directional","name": "vpnconnection1","admin_state_up": true,"tenant_id": "10039663455a446d8ba2cbb058b0f578","auth_mode": "psk","peer_cidrs": [],"mtu": 1500,"peer_ep_group_id": "9ad5a7e0-6dac-41b4-b20d-a7b8645fddf1","ikepolicy_id": "9b00d6b0-6c93-4ca5-9747-b8ade7bb514f","vpnservice_id": "5c561d9d-eaea-45f6-ae3e-08d1a7080828","dpd": {"action": "hold","interval": 30,"timeout": 120},"route_mode": "static","ipsecpolicy_id": "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1","local_ep_group_id": "3e1815dd-e212-43d0-8f13-b494fa553e68","peer_address": "172.24.4.226","peer_id": "172.24.4.226","id": "851f280f-5639-4ea3-81aa-e298525ab74b","description": ""}]}

