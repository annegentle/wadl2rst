=============================================================================
Trigger Node Action -  OpenStack Compute API v2.1
=============================================================================

Trigger Node Action
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_trigger_node_action_v1_nodes_node_id_actions.rst#request>`__
`Response <POST_trigger_node_action_v1_nodes_node_id_actions.rst#response>`__

.. code-block:: javascript

    POST /v1/nodes/{node_id}/actions

Triggers an action on a node.



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
|action                    |xsd:string *(Required)*  |The action to trigger.   |
|                          |                         |Each action takes a      |
|                          |                         |different set of         |
|                          |                         |parameters. Supported    |
|                          |                         |actions include:         |
|                          |                         |``check`` Check the      |
|                          |                         |health status of a node. |
|                          |                         |For example: {"check":   |
|                          |                         |{}} ``recover`` Recover  |
|                          |                         |a node from its current  |
|                          |                         |unhealthy status. For    |
|                          |                         |example: {"recover":     |
|                          |                         |{"operation": "rebuild"}}|
+--------------------------+-------------------------+-------------------------+





**Example Trigger Node Action: JSON request**


.. code::

    {"check": {}}


Response
^^^^^^^^^^^^^^^^^^




