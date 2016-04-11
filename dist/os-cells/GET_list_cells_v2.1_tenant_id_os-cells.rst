
List Cells
==========

.. rest_method:: GET /v2.1/{tenant_id}/os-cells

Lists cells.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../listCells.yaml

	- tenant_id: tenant_id








Response
^^^^^^^^





**Example List Cells: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-cells/cells-list-resp.json
   :language: javascript


