
List Keypairs
=============

`Request <GET_list_keypairs_v2.1_tenant_id_os-keypairs.rst#request>`__
`Response <GET_list_keypairs_v2.1_tenant_id_os-keypairs.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-keypairs

Lists keypairs that are associated with the account.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





**Example List Keypairs: JSON request**


.. code::

    {
        "keypairs": [
            {
                "keypair": {
                    "fingerprint": "7e:eb:ab:24:ba:d1:e1:88:ae:9a:fb:66:53:df:d3:bd",
                    "name": "keypair-50ca852e-273f-4cdc-8949-45feba200837",
                    "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkF3MX59OrlBs3dH5CU7lNmvpbrgZxSpyGjlnE8Flkirnc/Up22lpjznoxqeoTAwTW034k7Dz6aYIrZGmQwe2TkE084yqvlj45Dkyoj95fW/sZacm0cZNuL69EObEGHdprfGJQajrpz22NQoCD8TFB8Wv+8om9NH9Le6s+WPe98WC77KLw8qgfQsbIey+JawPWl4O67ZdL5xrypuRjfIPWjgy/VH85IXg/Z/GONZ2nxHgSShMkwqSFECAC5L3PHB+0+/12M/iikdatFSVGjpuHvkLOs3oe7m6HlOfluSJ85BzLWBbvva93qkGmLg4ZAc8rPh2O+YIsBUHNLLMM/oQp Generated-by-Nova\n"
                }
            }
        ]
    }
    

