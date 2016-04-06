
Show Certificate Details
========================

`Request <GET_show_certificate_details_v2.1_tenant_id_os-certificates_certificate_id_.rst#request>`__
`Response <GET_show_certificate_details_v2.1_tenant_id_os-certificates_certificate_id_.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-certificates/{certificate_id}

Shows details for a certificate.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id
	- certificate_id: certificate_id







Response
^^^^^^^^





**Example Show Certificate Details: JSON request**


.. code::

    {
        "certificate": {
            "data": "-----BEGIN CERTIFICATE-----\nMIICyzCCAjSgAwIBAgIJAJ8zSIxUp/m4MA0GCSqGSIb3DQEBBAUAME4xEjAQBgNV\nBAoTCU5PVkEgUk9PVDEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzETMBEGA1UECBMK\nQ2FsaWZvcm5pYTELMAkGA1UEBhMCVVMwHhcNMTIxMDE3MDEzMzM5WhcNMTMxMDE3\nMDEzMzM5WjBOMRIwEAYDVQQKEwlOT1ZBIFJPT1QxFjAUBgNVBAcTDU1vdW50YWlu\nIFZpZXcxEzARBgNVBAgTCkNhbGlmb3JuaWExCzAJBgNVBAYTAlVTMIGfMA0GCSqG\nSIb3DQEBAQUAA4GNADCBiQKBgQDXW4QfQQxJG4MqurqK8nU/Lge0mfNKxXj/Gwvg\n2sQVwxzmKfoxih8Nn6yt0yHMNjhoji1UoWI03TXUnPZRAZmsypGKZeBd7Y1ZOCPB\nXGZVGrQm+PB2kZU+3cD8fVKcueMLLeZ+LRt5d0njnoKhc5xjqMlfFPimHMba4OL6\nTnYzPQIDAQABo4GwMIGtMAwGA1UdEwQFMAMBAf8wHQYDVR0OBBYEFKyoKu4SMOFM\ngx5Ec7p0nrCkabvxMH4GA1UdIwR3MHWAFKyoKu4SMOFMgx5Ec7p0nrCkabvxoVKk\nUDBOMRIwEAYDVQQKEwlOT1ZBIFJPT1QxFjAUBgNVBAcTDU1vdW50YWluIFZpZXcx\nEzARBgNVBAgTCkNhbGlmb3JuaWExCzAJBgNVBAYTAlVTggkAnzNIjFSn+bgwDQYJ\nKoZIhvcNAQEEBQADgYEAXuvXlu1o/SVvykSLhHW8QiAY00yzN/eDzYmZGomgiuoO\n/x+ayVzbrz1UWZnBD+lC4hll2iELSmf22LjLoF+s/9NyPqHxGL3FrfatBkndaiF8\nAx/TMEyCPl7IQWi+3zzatqOKHSHiG7a9SGn/7o2aNTIWKVulfy5GvmbBjBM/0UE=\n-----END CERTIFICATE-----\n",
            "private_key": null
        }
    }
    

