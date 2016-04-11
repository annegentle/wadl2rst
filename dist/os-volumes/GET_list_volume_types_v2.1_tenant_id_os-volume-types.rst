
List Volume Types
=================

`Request <GET_list_volume_types_v2.1_tenant_id_os-volume-types.rst#request>`__
`Response <GET_list_volume_types_v2.1_tenant_id_os-volume-types.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-volume-types

Lists volume types.



Normal response codes: 200,,503,400,401,403,405,404

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^







Response
^^^^^^^^


.. rest_parameters:: ../listVolumeTypes.yaml

	- volume_types: volume_types
	- id: id
	- name: name
	- extra_specs: extra_specs




**Example List Volume Types: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-volumes/volume-types-list-resp.json
   :language: javascript

