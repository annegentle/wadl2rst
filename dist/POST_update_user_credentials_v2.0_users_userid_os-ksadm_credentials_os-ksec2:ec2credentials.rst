=============================================================================
Update User Credentials -  OpenStack Compute API v2.1
=============================================================================

Update User Credentials
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_update_user_credentials_v2.0_users_userid_os-ksadm_credentials_os-ksec2:ec2credentials.rst#request>`__
`Response <POST_update_user_credentials_v2.0_users_userid_os-ksadm_credentials_os-ksec2:ec2credentials.rst#response>`__

.. code-block:: javascript

    POST /v2.0/users/{userId}/OS-KSADM/credentials/OS-KSEC2:ec2Credentials

Updates credentials for a user.



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








**Example Update User Credentials: JSON request**


.. code::

    {"OS-KSEC2-ec2Credentials": {"username": "test_user","secret": "secretsecret","signature": "bbb"}}


Response
^^^^^^^^^^^^^^^^^^





**Example Update User Credentials: JSON request**


.. code::

    {"OS-KSEC2-ec2Credentials": {"username": "test_user","secret": "secretsecret","signature": "bbb"}}

