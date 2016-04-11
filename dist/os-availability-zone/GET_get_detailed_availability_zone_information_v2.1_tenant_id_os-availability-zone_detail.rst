
Get Detailed Availability Zone Information
==========================================

`Request <GET_get_detailed_availability_zone_information_v2.1_tenant_id_os-availability-zone_detail.rst#request>`__
`Response <GET_get_detailed_availability_zone_information_v2.1_tenant_id_os-availability-zone_detail.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-availability-zone/detail

Gets detailed availability zone information.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^





**Example Get detailed availability zone information: JSON response**


.. literalinclude:: ../../../doc/api_samples/os-availability-zone/availability-zone-show-details-resp.json
   :language: javascript

