=============================================================================
List Ipsec Policies -  OpenStack Compute API v2.1
=============================================================================

List Ipsec Policies
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_ipsec_policies_v2.0_vpn_ipsecpolicies.rst#request>`__
`Response <GET_list_ipsec_policies_v2.0_vpn_ipsecpolicies.rst#response>`__

.. code-block:: javascript

    GET /v2.0/vpn/ipsecpolicies

Lists all IPSec policies.



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
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |Owner of the VPN         |
|                          |                         |service. Only            |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the IPSec policy. Does   |
|                          |                         |not have to be unique.   |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the      |
|                          |                         |IPSec policy.            |
+--------------------------+-------------------------+-------------------------+
|transform_protocol        |xsd:string *(Required)*  |The transform protocol.  |
|                          |                         |A valid value is         |
|                          |                         |``ESP``, ``AH``, or ``AH-|
|                          |                         |ESP``. Default is        |
|                          |                         |``ESP``.                 |
+--------------------------+-------------------------+-------------------------+
|encapsulation_mode        |xsd:string *(Required)*  |The encapsulation mode.  |
|                          |                         |A valid value is         |
|                          |                         |``tunnel`` or            |
|                          |                         |``transport``. Default   |
|                          |                         |is ``tunnel``.           |
+--------------------------+-------------------------+-------------------------+
|auth_algorithm            |xsd:string *(Required)*  |The authentication       |
|                          |                         |algorithm. A valid value |
|                          |                         |is ``sha1``, which is    |
|                          |                         |the default.             |
+--------------------------+-------------------------+-------------------------+
|encryption_algorithm      |xsd:string *(Required)*  |The encryption           |
|                          |                         |algorithm. A valid value |
|                          |                         |is ``3des``, ``aes-      |
|                          |                         |128``, ``aes-192``,      |
|                          |                         |``aes-256``, and so on.  |
|                          |                         |Default is ``aes-128``.  |
+--------------------------+-------------------------+-------------------------+
|pfs                       |xsd:string *(Required)*  |Perfect forward secrecy  |
|                          |                         |(PFS). A valid value is  |
|                          |                         |``Group2``, ``Group5``,  |
|                          |                         |``Group14``, and so on.  |
|                          |                         |Default is ``Group5``.   |
+--------------------------+-------------------------+-------------------------+
|lifetime                  |xsd:dict *(Required)*    |The lifetime of the      |
|                          |                         |security association.    |
|                          |                         |The lifetime consists of |
|                          |                         |a unit and integer       |
|                          |                         |value. You can omit      |
|                          |                         |either the unit or value |
|                          |                         |portion of the lifetime. |
+--------------------------+-------------------------+-------------------------+
|units                     |xsd:string *(Required)*  |The units for the        |
|                          |                         |lifetime of the security |
|                          |                         |association. The         |
|                          |                         |lifetime consists of a   |
|                          |                         |unit and integer value.  |
|                          |                         |You can omit either the  |
|                          |                         |unit or value portion of |
|                          |                         |the lifetime. Default    |
|                          |                         |unit is seconds and      |
|                          |                         |default value is 3600.   |
+--------------------------+-------------------------+-------------------------+
|value                     |xsd:int *(Required)*     |The lifetime value, as a |
|                          |                         |positive integer. The    |
|                          |                         |lifetime consists of a   |
|                          |                         |unit and integer value.  |
|                          |                         |You can omit either the  |
|                          |                         |unit or value portion of |
|                          |                         |the lifetime. Default    |
|                          |                         |unit is seconds and      |
|                          |                         |default value is 3600.   |
+--------------------------+-------------------------+-------------------------+





**Example List Ipsec Policies: JSON request**


.. code::

    {"ipsecpolicies": [{"name": "ipsecpolicy1","transform_protocol": "esp","auth_algorithm": "sha1","encapsulation_mode": "tunnel","encryption_algorithm": "aes-128","pfs": "group14","tenant_id": "ccb81365fe36411a9011e90491fe1330","lifetime": {"units": "seconds","value": 3600},"id": "5291b189-fd84-46e5-84bd-78f40c05d69c","description": ""}]}

