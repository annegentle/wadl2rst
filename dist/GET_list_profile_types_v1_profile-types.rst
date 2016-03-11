=============================================================================
List Profile Types -  OpenStack Compute API v2.1
=============================================================================

List Profile Types
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_profile_types_v1_profile-types.rst#request>`__
`Response <GET_list_profile_types_v1_profile-types.rst#response>`__

.. code-block:: javascript

    GET /v1/profile-types

Lists supported profile types.



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





**Example List Profile Types: JSON request**


.. code::

    {"profile_types": [{"name": "os.heat.stack"},{"name": "os.heat.resource"},{"name": "os.nova.server"}]}

