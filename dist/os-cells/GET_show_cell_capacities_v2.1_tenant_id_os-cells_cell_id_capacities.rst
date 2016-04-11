
Show Cell Capacities
====================

.. rest_method:: GET /v2.1/{tenant_id}/os-cells/{cell_id}/capacities

Shows capacities for a cell.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^


URI Parameters
~~~~~~~~~~~~~~

.. rest_parameters:: ../showCellCapacities.yaml

	- tenant_id: tenant_id
	- cell_id: cell_id








Response
^^^^^^^^





**Example Show Cell Capacities: JSON request**


.. literalinclude:: ../../../doc/api_samples/os-cells/cells-capacities-show-resp.json
   :language: javascript


