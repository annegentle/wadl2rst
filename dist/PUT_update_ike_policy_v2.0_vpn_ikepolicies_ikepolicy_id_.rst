=============================================================================
Update Ike Policy -  OpenStack Compute API v2.1
=============================================================================

Update Ike Policy
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_ike_policy_v2.0_vpn_ikepolicies_ikepolicy_id_.rst#request>`__
`Response <PUT_update_ike_policy_v2.0_vpn_ikepolicies_ikepolicy_id_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/vpn/ikepolicies/{ikepolicy_id}

Updates policy settings in an IKE policy.



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
|{ikepolicy_id}            |csapi:UUID               |The UUID of the IKE      |
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|ikepolicy                 |xsd:dict *(Required)*    |An ``ikepolicy`` object. |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the IKE policy. Does not |
|                          |                         |have to be unique.       |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the IKE  |
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+
|auth_algorithm            |xsd:string *(Required)*  |The authentication hash  |
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
|phase1_negotiation_mode   |xsd:string *(Required)*  |The IKE mode. A valid    |
|                          |                         |value is ``main``, which |
|                          |                         |is the default.          |
+--------------------------+-------------------------+-------------------------+
|pfs                       |xsd:string *(Required)*  |Perfect forward secrecy  |
|                          |                         |(PFS). A valid value is  |
|                          |                         |``Group2``, ``Group5``,  |
|                          |                         |``Group14``, and so on.  |
|                          |                         |Default is ``Group5``.   |
+--------------------------+-------------------------+-------------------------+
|ike_version               |xsd:string *(Required)*  |The IKE version. A valid |
|                          |                         |value is ``v1`` or       |
|                          |                         |``v2``. Default is       |
|                          |                         |``v1``.                  |
+--------------------------+-------------------------+-------------------------+
|lifetime                  |xsd:dict *(Required)*    |The lifetime of the      |
|                          |                         |security association.    |
|                          |                         |The lifetime consists of |
|                          |                         |a unit and integer       |
|                          |                         |value. You can omit      |
|                          |                         |either the unit or value |
|                          |                         |portion of the lifetime. |
|                          |                         |Default unit is seconds  |
|                          |                         |and default value is     |
|                          |                         |3600.                    |
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





**Example Update Ike Policy: JSON request**


.. code::

    {"ikepolicy": {"encryption_algorithm": "aes-256"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|ikepolicy                 |xsd:dict *(Required)*    |An ``ikepolicy`` object. |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID for the IKE     |
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+
|tenant_id                 |csapi:UUID *(Required)*  |The owner of the VPN     |
|                          |                         |service. Only            |
|                          |                         |administrative users can |
|                          |                         |specify a tenant UUID    |
|                          |                         |other than their own.    |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |Human-readable name for  |
|                          |                         |the IKE policy. Does not |
|                          |                         |have to be unique.       |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |Human-readable           |
|                          |                         |description for the IKE  |
|                          |                         |policy.                  |
+--------------------------+-------------------------+-------------------------+
|auth_algorithm            |xsd:string *(Required)*  |The authentication hash  |
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
|phase1_negotiation_mode   |xsd:string *(Required)*  |The IKE mode. A valid    |
|                          |                         |value is ``main``, which |
|                          |                         |is the default.          |
+--------------------------+-------------------------+-------------------------+
|pfs                       |xsd:string *(Required)*  |Perfect forward secrecy  |
|                          |                         |(PFS). A valid value is  |
|                          |                         |``Group2``, ``Group5``,  |
|                          |                         |``Group14``, and so on.  |
|                          |                         |Default is ``Group5``.   |
+--------------------------+-------------------------+-------------------------+
|ike_version               |xsd:string *(Required)*  |The IKE version. A valid |
|                          |                         |value is ``v1`` or       |
|                          |                         |``v2``. Default is       |
|                          |                         |``v1``.                  |
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





**Example Update Ike Policy: JSON request**


.. code::

    {"ikepolicy": {"name": "ikepolicy1","tenant_id": "ccb81365fe36411a9011e90491fe1330","auth_algorithm": "sha1","encryption_algorithm": "aes-256","pfs": "group5","phase1_negotiation_mode": "main","lifetime": {"units": "seconds","value": 3600},"ike_version": "v1","id": "5522aff7-1b3c-48dd-9c3c-b50f016b73db","description": ""}}

