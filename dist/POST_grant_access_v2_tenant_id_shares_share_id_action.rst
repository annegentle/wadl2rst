=============================================================================
Grant Access -  OpenStack Compute API v2.1
=============================================================================

Grant Access
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_grant_access_v2_tenant_id_shares_share_id_action.rst#request>`__
`Response <POST_grant_access_v2_tenant_id_shares_share_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/shares/{share_id}/action

Grants access to a share.



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
|access_level              |xsd:string *(Required)*  |The access level to the  |
|                          |                         |share. To grant or deny  |
|                          |                         |access to a share, you   |
|                          |                         |specify one of the       |
|                          |                         |following share access   |
|                          |                         |levels: ``rw``. Read and |
|                          |                         |write (RW) access.       |
|                          |                         |``ro``. Read-only (RO)   |
|                          |                         |access.                  |
+--------------------------+-------------------------+-------------------------+
|access_type               |xsd:string *(Required)*  |The access rule type. A  |
|                          |                         |valid value for the      |
|                          |                         |share access rule type   |
|                          |                         |is one of the following  |
|                          |                         |values: ``ip``.          |
|                          |                         |Authenticates an         |
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
|access_to                 |xsd:string *(Required)*  |The value that defines   |
|                          |                         |the access. The back end |
|                          |                         |grants or denies the     |
|                          |                         |access to it. A valid    |
|                          |                         |value is one of these    |
|                          |                         |values: ``ip``.          |
|                          |                         |Authenticates an         |
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





**Example Grant Access: JSON request**


.. code::

    {"os-allow_access": {"access_level": "rw","access_type": "ip","access_to": "0.0.0.0/0"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|id              |csapi:UUID     |The access rule ID.                          |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|share_id        |csapi:UUID     |The UUID of the share to which you are       |
|                |*(Required)*   |granted or denied access.                    |
+----------------+---------------+---------------------------------------------+
|created_at      |xsd:dateTime   |The date and time stamp when the access rule |
|                |*(Required)*   |was created. The date and time stamp format  |
|                |               |is `ISO 8601                                 |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+
|updated_at      |xsd:dateTime   |The date and time stamp when the access rule |
|                |*(Required)*   |was updated. The date and time stamp format  |
|                |               |is `ISO 8601                                 |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``. If the access rule was  |
|                |               |never updated, this value is ``null``.       |
+----------------+---------------+---------------------------------------------+
|access_type     |xsd:string     |The rule access type.                        |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|access_to       |xsd:string     |The access that the back end grants or       |
|                |*(Required)*   |denies. A valid value for the share access   |
|                |               |rule type is one of these values: ``ip``.    |
|                |               |Authenticates an instance through its IP     |
|                |               |address. A valid format is ``XX.XX.XX.XX``   |
|                |               |or ``XX.XX.XX.XX/XX``. For example           |
|                |               |``0.0.0.0/0``. ``cert``. Authenticates an    |
|                |               |instance through a TLS certificate. Specify  |
|                |               |the TLS identity as the IDENTKEY. A valid    |
|                |               |value is any string up to 64 characters long |
|                |               |in the common name (CN) of the certificate.  |
|                |               |The meaning of a string depends on its       |
|                |               |interpretation. ``user``. Authenticates by a |
|                |               |user or group name. A valid value is an      |
|                |               |alphanumeric string that can contain some    |
|                |               |special characters and is from 4 to 32       |
|                |               |characters long.                             |
+----------------+---------------+---------------------------------------------+
|access_level    |xsd:string     |The share access level.                      |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+





**Example Grant Access: JSON request**


.. code::

    {"access": {"share_id": "406ea93b-32e9-4907-a117-148b3945749f","created_at": "2015-09-07T09:14:48.000000","updated_at": null,"access_type": "ip","access_to": "0.0.0.0/0","access_level": "rw","id": "a25b2df3-90bd-4add-afa6-5f0dbbd50452"}}

