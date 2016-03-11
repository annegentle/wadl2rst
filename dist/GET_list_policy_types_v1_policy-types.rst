=============================================================================
List Policy Types -  OpenStack Compute API v2.1
=============================================================================

List Policy Types
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_policy_types_v1_policy-types.rst#request>`__
`Response <GET_list_policy_types_v1_policy-types.rst#response>`__

.. code-block:: javascript

    GET /v1/policy-types

Lists all supported policy types.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^





**Example List Policy Types: JSON request**


.. code::

    {"policy_types": [{"name": "ScalingPolicy"},{"name": "PlacementPolicy"},{"name": "DeletionPolicy"},{"name": "LoadBalancingPolicy"},{"name": "HealthPolicy"},{"name": "UpdatePolicy"}]}

