
List Api Versions
=================

.. rest_method:: GET /

Lists information about all Compute API versions.



Normal response codes: 200,300

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^









Response
^^^^^^^^





**Example List Api Versions: JSON request**


.. literalinclude:: ../../../doc/api_samples/versions/versions-list-resp.json
   :language: javascript


