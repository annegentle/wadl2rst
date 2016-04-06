
List Cells With Details
=======================

`Request <GET_list_cells_with_details_v2.1_tenant_id_os-cells.rst#request>`__
`Response <GET_list_cells_with_details_v2.1_tenant_id_os-cells.rst#response>`__

.. rest_method:: GET /v2.1/{tenant_id}/os-cells

Lists cells with details.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



Normal response codes: 200,501

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^

.. rest_parameters:: parameters.yaml

	- tenant_id: tenant_id







Response
^^^^^^^^





**Example List Cells With Details: JSON request**


.. code::

    {
        "cells": []
    }
    

