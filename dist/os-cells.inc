.. -*- rst -*-
==============================
 Cells (os-cells, capacities)
==============================

Adds neighbor cells, lists neighbor cells, and shows the capabilities of
the local cell.

List Cells
==========

.. rest_method:: GET /v2.1/{tenant_id}/os-cells

Lists cells.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id







Response
--------





**Example List Cells: JSON request**


.. literalinclude:: ../../doc/api_samples/os-cells/cells-list-resp.json
   :language: javascript


List Cells With Details
=======================

.. rest_method:: GET /v2.1/{tenant_id}/os-cells

Lists cells with details.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id







Response
--------





**Example List Cells With Details: JSON request**


.. literalinclude:: ../../doc/api_samples/os-cells/cells-list-empty-resp.json
   :language: javascript


Show Cell Data
==============

.. rest_method:: GET /v2.1/{tenant_id}/os-cells/{cell_id}

Shows data for a cell.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id
  - cell_id: cell_id







Response
--------





**Example Show Cell Data: JSON request**


.. literalinclude:: ../../doc/api_samples/os-cells/cell-show-resp.json
   :language: javascript


Show Cell Capacities
====================

.. rest_method:: GET /v2.1/{tenant_id}/os-cells/{cell_id}/capacities

Shows capacities for a cell.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
-------


.. rest_parameters:: parameters.yaml

  - tenant_id: tenant_id
  - cell_id: cell_id







Response
--------





**Example Show Cell Capacities: JSON request**


.. literalinclude:: ../../doc/api_samples/os-cells/cells-capacities-show-resp.json
   :language: javascript


