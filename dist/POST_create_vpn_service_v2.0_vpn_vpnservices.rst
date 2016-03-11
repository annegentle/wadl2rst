=============================================================================
Create Vpn Service -  OpenStack Compute API v2.1
=============================================================================

Create Vpn Service
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_vpn_service_v2.0_vpn_vpnservices.rst#request>`__
`Response <POST_create_vpn_service_v2.0_vpn_vpnservices.rst#response>`__

.. code-block:: javascript

    POST /v2.0/vpn/vpnservices

Creates a VPN service.

The service is associated with a router. After you create the service, it can contain multiple VPN connections.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






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
|tenant_id                 |csapi:UUID *(Required)*  |Owner of the VPN         |
|                          |                         |service. Only            |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+
|subnet_id                 |csapi:UUID *(Required)*  |(Deprecated) The subnet  |
|                          |                         |where the tenant wants   |
|                          |                         |the VPN service.         |
+--------------------------+-------------------------+-------------------------+
|router_id                 |csapi:UUID *(Required)*  |The UUID of the router   |
|                          |                         |to which the VPN service |
|                          |                         |is inserted.             |
+--------------------------+-------------------------+-------------------------+





**Example Create Vpn Service: JSON request**


.. code::

    {"vpnservice": {"subnet_id": null,"router_id": "66e3b16c-8ce5-40fb-bb49-ab6d8dc3f2aa","name": "myservice","admin_state_up": true}}


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





**Example Create Vpn Service: JSON request**


.. code::

    {"vpnservice": {"router_id": "66e3b16c-8ce5-40fb-bb49-ab6d8dc3f2aa","status": "PENDING_CREATE","name": "myservice","external_v6_ip": "2001:db8::1","admin_state_up": true,"subnet_id": null,"tenant_id": "10039663455a446d8ba2cbb058b0f578","external_v4_ip": "172.32.1.11","id": "5c561d9d-eaea-45f6-ae3e-08d1a7080828","description": ""}}

