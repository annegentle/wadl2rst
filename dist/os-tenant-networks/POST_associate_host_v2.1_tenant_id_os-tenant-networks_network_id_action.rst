=============================================================================
Associate Host -  OpenStack Compute API v2.1
=============================================================================

Associate Host
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_associate_host_v2.1_tenant_id_os-tenant-networks_network_id_action.rst#request>`__
`Response <POST_associate_host_v2.1_tenant_id_os-tenant-networks_network_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-tenant-networks/{network_id}/action

Associates a network with a host.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
|{network_id}              |csapi:UUID               |The UUID of the network. |
+--------------------------+-------------------------+-------------------------+








**Example Associate Host: JSON request**


.. code::

    {
        "associate_host": "testHost"
    }
    


Response
^^^^^^^^^^^^^^^^^^




