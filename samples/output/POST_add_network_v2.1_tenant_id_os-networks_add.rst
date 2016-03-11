=============================================================================
Add Network -  OpenStack Compute API v2.1
=============================================================================

Add Network
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_add_network_v2.1_tenant_id_os-networks_add.rst#request>`__
`Response <POST_add_network_v2.1_tenant_id_os-networks_add.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-networks/add

Adds a network to a project.

Policy defaults enable only users with the administrative role to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








**Example Add Network: JSON request**


.. code::

    {
        "id": "1"
    }
    


Response
^^^^^^^^^^^^^^^^^^




