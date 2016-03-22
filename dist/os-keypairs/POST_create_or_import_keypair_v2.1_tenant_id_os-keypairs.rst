=============================================================================
Create Or Import Keypair -  OpenStack Compute API v2.1
=============================================================================

Create Or Import Keypair
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_or_import_keypair_v2.1_tenant_id_os-keypairs.rst#request>`__
`Response <POST_create_or_import_keypair_v2.1_tenant_id_os-keypairs.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-keypairs

Generates or imports a keypair.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The name to associate    |
|                          |                         |with the keypair.        |
+--------------------------+-------------------------+-------------------------+
|public_key                |xsd:string *(Required)*  |The public ssh key to    |
|                          |                         |import. If you omit this |
|                          |                         |value, a key is          |
|                          |                         |generated.               |
+--------------------------+-------------------------+-------------------------+





**Example Create Or Import Keypair: JSON request**


.. code::

    {
        "keypair": {
            "name": "keypair-d20a3d59-9433-4b79-8726-20b431d89c78",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDx8nkQv/zgGgB4rMYmIf+6A4l6Rr+o/6lHBQdW5aYd44bd8JttDCE/F/pNRr0lRE+PiqSPO8nDPHw0010JeMH9gYgnnFlyY3/OcJ02RhIPyyxYpv9FhY+2YiUkpwFOcLImyrxEsYXpD/0d3ac30bNH6Sw9JD9UZHYcpSxsIbECHw== Generated-by-Nova"
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create Or Import Keypair: JSON request**


.. code::

    {
        "keypair": {
            "fingerprint": "1e:2c:9b:56:79:4b:45:77:f9:ca:7a:98:2c:b0:d5:3c",
            "name": "keypair-803a1926-af78-4b05-902a-1d6f7a8d9d3e",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDx8nkQv/zgGgB4rMYmIf+6A4l6Rr+o/6lHBQdW5aYd44bd8JttDCE/F/pNRr0lRE+PiqSPO8nDPHw0010JeMH9gYgnnFlyY3/OcJ02RhIPyyxYpv9FhY+2YiUkpwFOcLImyrxEsYXpD/0d3ac30bNH6Sw9JD9UZHYcpSxsIbECHw== Generated-by-Nova",
            "user_id": "fake"
        }
    }
    

