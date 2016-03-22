=============================================================================
List Cells With Details -  OpenStack Compute API v2.1
=============================================================================

List Cells With Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_cells_with_details_v2.1_tenant_id_os-cells.rst#request>`__
`Response <GET_list_cells_with_details_v2.1_tenant_id_os-cells.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-cells

Lists cells with details.

When cells are not enabled, the call returns the ``Not Implemented (501)`` response code.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|501                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Cells With Details: JSON request**


.. code::

    {
        "cells": []
    }
    

