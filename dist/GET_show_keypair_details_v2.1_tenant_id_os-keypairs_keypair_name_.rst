=============================================================================
Show Keypair Details -  OpenStack Compute API v2.1
=============================================================================

Show Keypair Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_keypair_details_v2.1_tenant_id_os-keypairs_keypair_name_.rst#request>`__
`Response <GET_show_keypair_details_v2.1_tenant_id_os-keypairs_keypair_name_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-keypairs/{keypair_name}

Shows details for a keypair that is associated with the account.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{keypair_name}            |xsd:string               |The keypair name.        |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Keypair Details: JSON request**


.. code::

    {
        "keypair": {
            "fingerprint": "44:fe:29:6e:23:14:b9:53:5b:65:82:58:1c:fe:5a:c3",
            "name": "keypair-6638abdb-c4e8-407c-ba88-c8dd7cc3c4f1",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1HTrHCbb9NawNLSV8N6tSa8i637+EC2dA+lsdHHfQlT54t+N0nHhJPlKWDLhc579j87vp6RDFriFJ/smsTnDnf64O12z0kBaJpJPH2zXrBkZFK6q2rmxydURzX/z0yLSCP77SFJ0fdXWH2hMsAusflGyryHGX20n+mZK6mDrxVzGxEz228dwQ5G7Az5OoZDWygH2pqPvKjkifRw0jwUKf3BbkP0QvANACOk26cv16mNFpFJfI1N3OC5lUsZQtKGR01ptJoWijYKccqhkAKuo902tg/qup58J5kflNm7I61sy1mJon6SGqNUSfoQagqtBH6vd/tU1jnlwZ03uUroAL Generated-by-Nova\n",
            "user_id": "fake",
            "deleted": false,
            "created_at": "2014-05-07T12:06:13.681238",
            "updated_at": null,
            "deleted_at": null,
            "id": 1
        }
    }
    

