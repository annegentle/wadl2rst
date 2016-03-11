=============================================================================
Trigger Cluster Action -  OpenStack Compute API v2.1
=============================================================================

Trigger Cluster Action
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_trigger_cluster_action_v1_clusters_cluster_id_actions.rst#request>`__
`Response <POST_trigger_cluster_action_v1_clusters_cluster_id_actions.rst#response>`__

.. code-block:: javascript

    POST /v1/clusters/{cluster_id}/actions

Triggers an action on a cluster.



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
|{cluster_id}              |csapi:UUID *(Required)*  |The UUID of the cluster. |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|action                    |xsd:string *(Required)*  |The action to trigger.   |
|                          |                         |Each action takes a      |
|                          |                         |different set of         |
|                          |                         |parameters. Supported    |
|                          |                         |actions include:         |
|                          |                         |``add_nodes`` Add one or |
|                          |                         |more nodes, as a list,   |
|                          |                         |to a cluster. For        |
|                          |                         |example: {"add_nodes":   |
|                          |                         |{"nodes": ["node1"]}}    |
|                          |                         |``del_nodes`` Delete one |
|                          |                         |or more nodes, as a      |
|                          |                         |list, from a cluster.    |
|                          |                         |For example:             |
|                          |                         |{"del_nodes": {"nodes":  |
|                          |                         |["node1"]}}              |
|                          |                         |``scale_out`` Enlarge    |
|                          |                         |the cluster by ``count`` |
|                          |                         |number of nodes. For     |
|                          |                         |example: {"scale_out":   |
|                          |                         |{"count": "1"}}          |
|                          |                         |``scale_in`` Shrink the  |
|                          |                         |cluster by ``count``     |
|                          |                         |number of nodes. For     |
|                          |                         |example: {"scale_in":    |
|                          |                         |{"count": "2"}}          |
|                          |                         |``resize`` Change the    |
|                          |                         |size of the cluster by   |
|                          |                         |``adjustment_type``,     |
|                          |                         |``number``,              |
|                          |                         |``min_step``,            |
|                          |                         |``min_size``,            |
|                          |                         |``max_size``, or         |
|                          |                         |``strict`` values. For   |
|                          |                         |example: {"resize":      |
|                          |                         |{"adjustment_type":      |
|                          |                         |"CHANGE_IN_PERCENTAGE",  |
|                          |                         |"max_size": 20,          |
|                          |                         |"min_step": 1,           |
|                          |                         |"min_size": 5,"number":  |
|                          |                         |20,"strict": true}}      |
|                          |                         |``check`` Check the      |
|                          |                         |health status of a       |
|                          |                         |cluster. For example:    |
|                          |                         |{"check": {}}            |
|                          |                         |``recover`` Recover a    |
|                          |                         |cluster from its current |
|                          |                         |unhealthy status. For    |
|                          |                         |example: {"recover":     |
|                          |                         |{"operation":            |
|                          |                         |"rebuild"}}              |
|                          |                         |``policy_attach`` Attach |
|                          |                         |a policy to a cluster.   |
|                          |                         |The request body         |
|                          |                         |contains parameters for  |
|                          |                         |the policy attachment:   |
|                          |                         |{"policy_attach":        |
|                          |                         |{"enabled": true,        |
|                          |                         |"policy_id": "lb001"}}   |
|                          |                         |``policy_detach`` Detach |
|                          |                         |a policy from a cluster. |
|                          |                         |The request body         |
|                          |                         |contains the ID of the   |
|                          |                         |policy:                  |
|                          |                         |{"policy_detach":        |
|                          |                         |{"policy_id": "lb001"}}  |
|                          |                         |``policy_update`` Update |
|                          |                         |the policy attachment.   |
|                          |                         |Specify the policy ID    |
|                          |                         |and property settings in |
|                          |                         |the request body:        |
|                          |                         |{"policy_update":        |
|                          |                         |{"enabled": false,       |
|                          |                         |"policy_id": "lb001"}}   |
+--------------------------+-------------------------+-------------------------+





**Example Trigger Cluster Action: JSON request**


.. code::

    {"add_nodes": {"nodes": ["node1"]}}


Response
^^^^^^^^^^^^^^^^^^




