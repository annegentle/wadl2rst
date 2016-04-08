
Show Server Password
====================

`Request <GET_show_server_password_v2.1_tenant_id_servers_server_id_os-server-password.rst#request>`__
`Response <GET_show_server_password_v2.1_tenant_id_servers_server_id_os-server-password.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/servers/{server_id}/os-server-password

Shows the administrative password for a server.

This operation calls the metadata service to query metadata information and does not read password information from the server itself.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Server Password: JSON request**


.. code::

    {
        "password": "xlozO3wLCBRWAa2yDjCCVx8vwNPypxnypmRYDa/zErlQ+EzPe1S/Gz6nfmC52mOlOSCRuUOmG7kqqgejPof6M7bOezS387zjq4LSvvwp28zUknzy4YzfFGhnHAdai3TxUJ26pfQCYrq8UTzmKF2Bq8ioSEtVVzM0A96pDh8W2i7BOz6MdoiVyiev/I1K2LsuipfxSJR7Wdke4zNXJjHHP2RfYsVbZ/k9ANu+Nz4iIH8/7Cacud/pphH7EjrY6a4RZNrjQskrhKYed0YERpotyjYk1eDtRe72GrSiXteqCM4biaQ5w3ruS+AcX//PXk3uJ5kC7d67fPXaVz4WaQRYMg=="
    }
    

