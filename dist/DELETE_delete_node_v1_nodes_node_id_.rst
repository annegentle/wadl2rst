=============================================================================
Delete Node -  OpenStack Compute API v2.1
=============================================================================

Delete Node
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_node_v1_nodes_node_id_.rst#request>`__
`Response <DELETE_delete_node_v1_nodes_node_id_.rst#response>`__

.. code-block:: javascript

    DELETE /v1/nodes/{node_id}

Deletes a node.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{node_id}                 |csapi:UUID *(Required)*  |The UUID of the node.    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




