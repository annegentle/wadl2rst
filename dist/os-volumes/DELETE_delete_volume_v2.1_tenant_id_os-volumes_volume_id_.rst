
Delete Volume
=============

`Request <DELETE_delete_volume_v2.1_tenant_id_os-volumes_volume_id_.rst#request>`__
`Response <DELETE_delete_volume_v2.1_tenant_id_os-volumes_volume_id_.rst#response>`__

.. rest_method:: DELETE /v2.1/{tenant_id}/os-volumes/{volume_id}

Deletes a volume.



Normal response codes: 202,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Delete Volume: JSON request**


.. code::

    HTTP/1.1 202 Accepted
    Content-Type: text/html; charset=UTF-8
    Content-Length: 0
    Date: Fri, 05 Dec 2014 00:39:32 GMT
    

