=============================================================================
Update Vpn Service -  OpenStack Compute API v2.1
=============================================================================

Update Vpn Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_vpn_service_v2.0_vpn_vpnservices_service_id_.rst#request>`__
`Response <PUT_update_vpn_service_v2.0_vpn_vpnservices_service_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/vpn/vpnservices/{service_id}

Updates a VPN service.

Updates the attributes of a VPN service. You cannot update a service with a ``PENDING_*`` status.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|vpnservice                |xsd:dict *(Required)*    |A ``vpnservice`` object. |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the VPN service. Does    |
|                          |                         |not have to be unique.   |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the VPN  |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the VPN service,      |
|                          |                         |which is up ( ``true`` ) |
|                          |                         |or down ( ``false`` ).   |
|                          |                         |If down, connections on  |
|                          |                         |service are not active.  |
+--------------------------+-------------------------+-------------------------+





**Example Update Vpn Service: JSON request**


.. code::

    {"vpnservice": {"description": "Updated description"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|vpnservice                |xsd:dict *(Required)*    |A ``vpnservice`` object. |
+--------------------------+-------------------------+-------------------------+
|router_id                 |csapi:UUID *(Required)*  |The UUID of the router   |
|                          |                         |into which the VPN       |
|                          |                         |service is inserted.     |
+--------------------------+-------------------------+-------------------------+
|status                    |xsd:string *(Required)*  |Indicates whether IPSec  |
|                          |                         |VPN service is currently |
|                          |                         |operational. Value is    |
|                          |                         |``ACTIVE``, ``DOWN``,    |
|                          |                         |``BUILD``, ``ERROR``,    |
|                          |                         |``PENDING_CREATE``,      |
|                          |                         |``PENDING_UPDATE``, or   |
|                          |                         |``PENDING_DELETE``.      |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the VPN service. Does    |
|                          |                         |not have to be unique.   |
+--------------------------+-------------------------+-------------------------+
|admin_state_up            |xsd:boolean *(Required)* |The administrative state |
|                          |                         |of the VPN service,      |
|                          |                         |which is up ( ``true`` ) |
|                          |                         |or down ( ``false`` ).   |
|                          |                         |If down, the port does   |
|                          |                         |not forward packets.     |
+--------------------------+-------------------------+-------------------------+
|external_v4_ip            |xsd:string *(Required)*  |Read-only external       |
|                          |                         |(public) IPv4 address    |
|                          |                         |that is used for the VPN |
|                          |                         |service. The VPN plugin  |
|                          |                         |sets this address if an  |
|                          |                         |IPv4 interface is        |
|                          |                         |available.               |
+--------------------------+-------------------------+-------------------------+
|external_v6_ip            |xsd:string *(Required)*  |Read-only external       |
|                          |                         |(public) IPv6 address    |
|                          |                         |that is used for the VPN |
|                          |                         |service. The VPN plugin  |
|                          |                         |sets this address if an  |
|                          |                         |IPv6 interface is        |
|                          |                         |available.               |
+--------------------------+-------------------------+-------------------------+
|subnet_id                 |csapi:UUID *(Required)*  |(Deprecated) The subnet  |
|                          |                         |where the tenant wants   |
|                          |                         |the VPN service.         |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The owner of the VPN     |
|                          |                         |service. Only            |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID for the VPN     |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the VPN  |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+





**Example Update Vpn Service: JSON request**


.. code::

    {"vpnservice": {"router_id": "881b7b30-4efb-407e-a162-5630a7af3595","status": "ACTIVE","name": "myvpn","admin_state_up": true,"subnet_id": null,"tenant_id": "26de9cd6cae94c8cb9f79d660d628e1f","id": "41bfef97-af4e-4f6b-a5d3-4678859d2485","description": "Updated description"}}

