=============================================================================
Create Policy -  OpenStack Compute API v2.1
=============================================================================

Create Policy
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_policy_v1_policies.rst#request>`__
`Response <POST_create_policy_v1_policies.rst#response>`__

.. code-block:: javascript

    POST /v1/policies

Creates a policy.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^






This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|policy                    |xsd:dict *(Required)*    |A map with keys and      |
|                          |                         |values that specify the  |
|                          |                         |details for the policy   |
|                          |                         |to be created:           |
+--------------------------+-------------------------+-------------------------+
|name                      |xsd:string *(Required)*  |The name for the policy. |
+--------------------------+-------------------------+-------------------------+
|spec                      |xsd:dict *(Required)*    |A detailed specification |
|                          |                         |based on the policy type.|
+--------------------------+-------------------------+-------------------------+
|level                     |xsd:int *(Required)*     |An integer value that    |
|                          |                         |represents the default   |
|                          |                         |enforcement level.       |
+--------------------------+-------------------------+-------------------------+
|cooldown                  |xsd:int *(Required)*     |The cooldown value, in   |
|                          |                         |seconds.                 |
+--------------------------+-------------------------+-------------------------+





**Example Create Policy: JSON request**


.. code::

    {"policy": {"name": "sp001","spec": {"properties": {"adjustment": {"min_step": 1,"number": 1,"type": "CHANGE_IN_CAPACITY"},"event": "CLUSTER_SCALE_IN"},"type": "senlin.policy.scaling","version": "1.0"}}}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|policy                    |xsd:dict *(Required)*    |A map with a set of keys |
|                          |                         |and values that provides |
|                          |                         |the details of the       |
|                          |                         |policy. Policy create    |
|                          |                         |response``id`` An unique |
|                          |                         |ID for the newly created |
|                          |                         |policy. ``name`` Name    |
|                          |                         |for the newly created    |
|                          |                         |policy. ``type`` Name of |
|                          |                         |policy type referenced   |
|                          |                         |by the policy. ``spec``  |
|                          |                         |Detailed specification   |
|                          |                         |based on the policy      |
|                          |                         |type. ``created_at`` The |
|                          |                         |UTC date and time stamp  |
|                          |                         |when the policy was      |
|                          |                         |created. ``updated_at``  |
|                          |                         |The UTC date and time    |
|                          |                         |stamp when the policy    |
|                          |                         |was updated. ``domain``  |
|                          |                         |The ID of the domain to  |
|                          |                         |which the profile        |
|                          |                         |belongs. ``project`` The |
|                          |                         |ID of the project to     |
|                          |                         |which the profile        |
|                          |                         |belongs. ``user`` The ID |
|                          |                         |of the user who created  |
|                          |                         |the profile.             |
+--------------------------+-------------------------+-------------------------+





**Example Create Policy: JSON request**


.. code::

    {"policy": {"created_at": "2015-03-02T07:40:31","data": {},"domain": null,"id": "02f62195-2198-4797-b0a9-877632208527","name": "sp001","project": "42d9e9663331431f97b75e25136307ff","spec": {"properties": {"adjustment": {"best_effort": true,"min_step": 1,"number": 1,"type": "CHANGE_IN_CAPACITY"},"event": "CLUSTER_SCALE_IN"},"type": "senlin.policy.scaling","version": "1.0"},"type": "senlin.policy.scaling-1.0","updated_at": null,"user": "5e5bf8027826429c96af157f68dc9072"}}

