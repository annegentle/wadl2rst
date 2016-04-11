
Create Certificate
==================

`Request <POST_create_certificate_v2.1_tenant_id_os-certificates.rst#request>`__
`Response <POST_create_certificate_v2.1_tenant_id_os-certificates.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/os-certificates

Creates a certificate.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Create Certificate: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-certificates/certificate-create-resp.json
   :language: javascript

