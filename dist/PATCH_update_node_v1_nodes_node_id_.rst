=============================================================================
Update Node -  OpenStack Compute API v2.1
=============================================================================

Update Node
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PATCH_update_node_v1_nodes_node_id_.rst#request>`__
`Response <PATCH_update_node_v1_nodes_node_id_.rst#response>`__

.. code-block:: javascript

    PATCH /v1/nodes/{node_id}

Updates a node.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|node                      |xsd:dict *(Required)*    |A map with detailed data |
|                          |                         |for the node. Node       |
|                          |                         |update request           |
|                          |                         |body``name`` New name    |
|                          |                         |for the node (optional). |
|                          |                         |``profile_id`` Name, ID, |
|                          |                         |or short ID of the new   |
|                          |                         |profile to use by the    |
|                          |                         |node. The new profile    |
|                          |                         |has to have the same     |
|                          |                         |profile type as that of  |
|                          |                         |the node (optional).     |
|                          |                         |``role`` The new role    |
|                          |                         |this node plays in a     |
|                          |                         |cluster (optional).      |
|                          |                         |``metadata`` A list of   |
|                          |                         |key-value pairs to       |
|                          |                         |attach to the updated    |
|                          |                         |node (optional).         |
+--------------------------+-------------------------+-------------------------+





**Example Update Node: JSON request**


.. code::

    {"node": {"name": "new_node_name"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|node                      |xsd:dict *(Required)*    |Detailed data for the    |
|                          |                         |node such as ``id``,     |
|                          |                         |``name``, ``status``,    |
|                          |                         |and so on.               |
+--------------------------+-------------------------+-------------------------+





**Example Update Node: JSON request**


.. code::

    {"node": {"action": "2366d440-c73e-4961-9254-6d1c3af7c167","cluster_id": null,"created_at": null,"data": {},"domain": null,"id": "0df0931b-e251-4f2e-8719-4ebfda3627ba","index": -1,"init_at": "2015-03-05T08:53:15","metadata": {},"name": "node009","physical_id": "","profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","role": "master","status": "ACTIVE","status_reason": "Update succeeded","updated_at": "2015-09-01T18:53:15","user": "5e5bf8027826429c96af157f68dc9072"}}

