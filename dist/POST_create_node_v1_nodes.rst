=============================================================================
Create Node -  OpenStack Compute API v2.1
=============================================================================

Create Node
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_node_v1_nodes.rst#request>`__
`Response <POST_create_node_v1_nodes.rst#response>`__

.. code-block:: javascript

    POST /v1/nodes

Creates a node.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|node                      |xsd:dict *(Required)*    |A map with detailed data |
|                          |                         |for the node. Node       |
|                          |                         |Create Request           |
|                          |                         |Body``name`` Name for    |
|                          |                         |the created node         |
|                          |                         |(required).              |
|                          |                         |``profile_id`` Name, ID, |
|                          |                         |or short ID of the       |
|                          |                         |profile used by the node |
|                          |                         |for creation (required). |
|                          |                         |``cluster_id`` Name, ID, |
|                          |                         |or short ID of the       |
|                          |                         |cluster the node lives   |
|                          |                         |in. If not specified,    |
|                          |                         |the node created will be |
|                          |                         |an orphaned node         |
|                          |                         |(optional). ``role`` A   |
|                          |                         |string indicating the    |
|                          |                         |role this node plays in  |
|                          |                         |a cluster (optional).    |
|                          |                         |``metadata`` A list of   |
|                          |                         |key-value pairs to       |
|                          |                         |attach to the newly      |
|                          |                         |created node (optional). |
+--------------------------+-------------------------+-------------------------+





**Example Create Node: JSON request**


.. code::

    {"node": {"cluster_id": null,"metadata": {},"name": "node009","profile_id": "mystack","role": "master"}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|node                      |xsd:dict *(Required)*    |Detailed data for the    |
|                          |                         |node, such as ``id``,    |
|                          |                         |``name``, ``status``,    |
|                          |                         |and so on.               |
+--------------------------+-------------------------+-------------------------+





**Example Create Node: JSON request**


.. code::

    {"node": {"action": "2366d440-c73e-4961-9254-6d1c3af7c167","cluster_id": null,"created_at": null,"data": {},"domain": null,"id": "0df0931b-e251-4f2e-8719-4ebfda3627ba","index": -1,"init_at": "2015-03-05T08:53:15","metadata": {},"name": "node009","physical_id": "","profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","role": "master","status": "INIT","status_reason": "Initializing","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

