.. -*- rst -*-
=====================================
 Root certificates (os-certificates)
=====================================

Creates and shows details for a root certificate.

Create Certificate
==================

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


Show Certificate Details
========================

.. rest_method:: GET /v2.1/{tenant_id}/os-certificates/{certificate_id}

Shows details for a certificate.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Show Certificate Details: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-certificates/certificate-show-root-resp.json
   :language: javascript


