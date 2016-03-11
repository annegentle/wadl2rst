=============================================================================
Grant Credential To User -  OpenStack Compute API v2.1
=============================================================================

Grant Credential To User
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_grant_credential_to_user_v2.0_users_userid_os-ksadm_credentials.rst#request>`__
`Response <POST_grant_credential_to_user_v2.0_users_userid_os-ksadm_credentials.rst#response>`__

.. code-block:: javascript

    POST /v2.0/users/{userId}/OS-KSADM/credentials

Grants a credential to a user.



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

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{user_id}                 |capi:UUID                |The UUID of the user.    |
+--------------------------+-------------------------+-------------------------+
|X-Auth-Token              |xsd:string *(Required)*  |A valid authentication   |
|                          |                         |token for an             |
|                          |                         |administrative user.     |
+--------------------------+-------------------------+-------------------------+








**Example Grant Credential To User: JSON request**


.. code::

    {"OS-KSEC2-ec2Credentials": {"username": "test_user","secret": "secretsecret","signature": "bbb"}}


Response
^^^^^^^^^^^^^^^^^^





**Example Grant Credential To User: JSON request**


.. code::

    {"OS-KSEC2-ec2Credentials": {"username": "test_user","secret": "secretsecret","signature": "bbb"}}

