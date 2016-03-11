=============================================================================
Show Node Details -  OpenStack Compute API v2.1
=============================================================================

Show Node Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_node_details_v1_nodes_node_id_.rst#request>`__
`Response <GET_show_node_details_v1_nodes_node_id_.rst#response>`__

.. code-block:: javascript

    GET /v1/nodes/{node_id}

Shows data for a node.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{node_id}                 |csapi:UUID *(Required)*  |The UUID of the node.    |
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|show_details              |xsd:boolean *(Required)* |Indicates whether the    |
|                          |                         |node details are         |
|                          |                         |returned. Default is     |
|                          |                         |``False``.               |
+--------------------------+-------------------------+-------------------------+







Response
^^^^^^^^^^^^^^^^^^





**Example Show Node Details: JSON request**


.. code::

    {"node": {"cluster_id": null,"created_at": "2015-02-10T12:03:16","data": {},"domain": null,"id": "d5779bb0-f0a0-49c9-88cc-6f078adb5a0b","index": -1,"init_at": "2015-02-10T12:03:13","metadata": {},"name": "node1","physical_id": "f41537fa-22ab-4bea-94c0-c874e19d0c80","profile_id": "edc63d0a-2ca4-48fa-9854-27926da76a4a","profile_name": "mystack","project": "6e18cc2bdbeb48a5b3cad2dc499f6804","role": null,"status": "ACTIVE","status_reason": "Creation succeeded","updated_at": "2015-03-04T04:58:27","user": "5e5bf8027826429c96af157f68dc9072"}}

