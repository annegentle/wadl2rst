=============================================================================
List Access Rules -  OpenStack Compute API v2.1
=============================================================================

List Access Rules
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_list_access_rules_v2_tenant_id_shares_share_id_action.rst#request>`__
`Response <POST_list_access_rules_v2_tenant_id_shares_share_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/shares/{share_id}/action

Lists access rules for a share.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{share_id}                |csapi:UUID               |The UUID of the share.   |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|X-Openstack-Manila-Api-   |xsd:string               |The HTTP header to       |
|Version                   |                         |specify a valid Shared   |
|                          |                         |File Systems API micro-  |
|                          |                         |version. For example,    |
|                          |                         |``"X-Openstack-Manila-   |
|                          |                         |Api-Version: 2.6"``. If  |
|                          |                         |you omit this header,    |
|                          |                         |the default micro-       |
|                          |                         |version is 2.0.          |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-access_list            |xsd:string *(Required)*  |The object of the access |
|                          |                         |rule. To list access     |
|                          |                         |rules, set this value to |
|                          |                         |``null``.                |
+--------------------------+-------------------------+-------------------------+





**Example List Access Rules: JSON request**


.. code::

    {"os-access_list": null}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|access_level              |xsd:string *(Required)*  |The share access level.  |
|                          |                         |A valid value is either: |
|                          |                         |``rw``. Read and write   |
|                          |                         |(RW) access. ``ro``.     |
|                          |                         |Read-only (RO) access.   |
+--------------------------+-------------------------+-------------------------+
|state                     |xsd:string *(Required)*  |The access rule state. A |
|                          |                         |valid value is           |
|                          |                         |``active`` or ``error``. |
+--------------------------+-------------------------+-------------------------+
|id                        |csapi:UUID *(Required)*  |The UUID of the access   |
|                          |                         |rule.                    |
+--------------------------+-------------------------+-------------------------+
|access_type               |xsd:string *(Required)*  |The access type of an    |
|                          |                         |access rule.             |
+--------------------------+-------------------------+-------------------------+
|access_to                 |xsd:string *(Required)*  |The access that the back |
|                          |                         |end grants or denies. A  |
|                          |                         |valid value for the      |
|                          |                         |share access rule type   |
|                          |                         |is one of these values:  |
|                          |                         |``ip``. Authenticates an |
|                          |                         |instance through its IP  |
|                          |                         |address. A valid format  |
|                          |                         |is ``XX.XX.XX.XX`` or    |
|                          |                         |``XX.XX.XX.XX/XX``. For  |
|                          |                         |example ``0.0.0.0/0``.   |
|                          |                         |``cert``. Authenticates  |
|                          |                         |an instance through a    |
|                          |                         |TLS certificate. Specify |
|                          |                         |the TLS identity as the  |
|                          |                         |IDENTKEY. A valid value  |
|                          |                         |is any string up to 64   |
|                          |                         |characters long in the   |
|                          |                         |common name (CN) of the  |
|                          |                         |certificate. The meaning |
|                          |                         |of a string depends on   |
|                          |                         |its interpretation.      |
|                          |                         |``user``. Authenticates  |
|                          |                         |by a user or group name. |
|                          |                         |A valid value is an      |
|                          |                         |alphanumeric string that |
|                          |                         |can contain some special |
|                          |                         |characters and is from 4 |
|                          |                         |to 32 characters long.   |
+--------------------------+-------------------------+-------------------------+





**Example List Access Rules: JSON request**


.. code::

    {"access_list": [{"access_level": "rw","state": "error","id": "507bf114-36f2-4f56-8cf4-857985ca87c1","access_type": "cert","access_to": "example.com"},{"access_level": "rw","state": "active","id": "a25b2df3-90bd-4add-afa6-5f0dbbd50452","access_type": "ip","access_to": "0.0.0.0/0"}]}

