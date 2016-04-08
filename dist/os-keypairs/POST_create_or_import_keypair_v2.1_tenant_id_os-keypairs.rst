
Create Or Import Keypair
========================

`Request <POST_create_or_import_keypair_v2.1_tenant_id_os-keypairs.rst#request>`__
`Response <POST_create_or_import_keypair_v2.1_tenant_id_os-keypairs.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-keypairs

Generates or imports a keypair.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: createOrImportKeypair.yaml

	- name: name
	- public_key: public_key




**Example Create Or Import Keypair: JSON request**


.. code::

    {
        "keypair": {
            "name": "keypair-d20a3d59-9433-4b79-8726-20b431d89c78",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDx8nkQv/zgGgB4rMYmIf+6A4l6Rr+o/6lHBQdW5aYd44bd8JttDCE/F/pNRr0lRE+PiqSPO8nDPHw0010JeMH9gYgnnFlyY3/OcJ02RhIPyyxYpv9FhY+2YiUkpwFOcLImyrxEsYXpD/0d3ac30bNH6Sw9JD9UZHYcpSxsIbECHw== Generated-by-Nova"
        }
    }
    


Response
^^^^^^^^





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
    

