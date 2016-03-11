=============================================================================
Create Trust -  OpenStack Compute API v2.1
=============================================================================

Create Trust
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_trust_v3_os-trust_trusts.rst#request>`__
`Response <POST_create_trust_v3_os-trust_trusts.rst#response>`__

.. code-block:: javascript

    POST /v3/OS-TRUST/trusts

Creates a trust.



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
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|413                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|415                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+-----------------+--------------+---------------------------------------------+
|Name             |Type          |Description                                  |
+=================+==============+=============================================+
|trust            |xsd:string    |A trust object.                              |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|oauth_expires_at |xsd:dateTime  |The date and time when a request token       |
|                 |*(Required)*  |expires. The date and time stamp format is   |
|                 |              |`ISO 8601                                    |
|                 |              |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                 |              |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                 |              |value, if included, is the time zone as an   |
|                 |              |offset from UTC. For example, ``2015-08-     |
|                 |              |27T09:49:58-05:00``. If the Identity API     |
|                 |              |does not include this attribute or its value |
|                 |              |is ``null``, the token never expires.        |
+-----------------+--------------+---------------------------------------------+
|impersonation    |xsd:boolean   |The impersonation flag. Default is false.    |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|project_id       |csapi:UUID    |The ID of the project.                       |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|remaining_uses   |xsd:boolean   |Remaining uses flag. Default is null.        |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|roles            |xsd:dict      |A roles object.                              |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|name             |xsd:string    |The role name.                               |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|trustee_user_id  |xsd:string    |The trustee user ID.                         |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|trustor_user_id  |xsd:string    |The trustor user ID.                         |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+





**Example Create Trust: JSON request**


.. code::

    {"trust": {"expires_at": "2014-12-30T23:59:59.999999Z","impersonation": false,"project_id": "'$PROJECT_ID'","roles": [{"name": "admin"}],"trustee_user_id": "'$DEMO_USER_ID'","trustor_user_id": "'$ADMIN_USER_ID'"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+-----------------+--------------+---------------------------------------------+
|Name             |Type          |Description                                  |
+=================+==============+=============================================+
|trust            |xsd:string    |A trust object.                              |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|oauth_expires_at |xsd:dateTime  |The date and time when a request token       |
|                 |*(Required)*  |expires. The date and time stamp format is   |
|                 |              |`ISO 8601                                    |
|                 |              |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                 |              |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                 |              |value, if included, is the time zone as an   |
|                 |              |offset from UTC. For example, ``2015-08-     |
|                 |              |27T09:49:58-05:00``. If the Identity API     |
|                 |              |does not include this attribute or its value |
|                 |              |is ``null``, the token never expires.        |
+-----------------+--------------+---------------------------------------------+
|id               |csapi:UUID    |The ID of the trust.                         |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|impersonation    |xsd:boolean   |The impersonation flag.                      |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|links            |xsd:dict      |Trust links.                                 |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|project_id       |csapi:UUID    |The ID of the project.                       |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|remaining_uses   |xsd:boolean   |Remaining uses flag.                         |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|roles            |xsd:dict      |A ``roles`` object. Includes ``id``,         |
|                 |*(Required)*  |``name``, and ``links`` for any roles.       |
+-----------------+--------------+---------------------------------------------+
|roles_links      |xsd:dict      |A roles links object. Includes ``next``,     |
|                 |*(Required)*  |``previous``, and ``self`` links for roles.  |
+-----------------+--------------+---------------------------------------------+
|trustee_user_id  |xsd:string    |The trustee user ID.                         |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+
|trustor_user_id  |xsd:string    |The trustor user ID.                         |
|                 |*(Required)*  |                                             |
+-----------------+--------------+---------------------------------------------+





**Example Create Trust: JSON request**


.. code::

    {"trust": {"expires_at": "2014-12-30T23:59:59.999999Z","id": "394998fa61f14736b1f0c1f322882949","impersonation": false,"links": {"self": "http://localhost:5000/v3/OS-TRUST/trusts/394998fa61f14736b1f0c1f322882949"},"project_id": "3d4c2c82bd5948f0bcab0cf3a7c9b48c","remaining_uses": null,"roles": [{"id": "c703057be878458588961ce9a0ce686b","links": {"self": "http://localhost:5000/v3/roles/c703057be878458588961ce9a0ce686b"},"name": "admin"}],"roles_links": {"next": null,"previous": null,"self": "http: //localhost:5000/v3/OS-TRUST/trusts/394998fa61f14736b1f0c1f322882949/roles"},"trustee_user_id": "269348fdd9374b8885da1418e0730af1","trustor_user_id": "3ec3164f750146be97f21559ee4d9c51"}}

