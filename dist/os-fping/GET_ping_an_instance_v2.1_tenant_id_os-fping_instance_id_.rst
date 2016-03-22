=============================================================================
Ping An Instance -  OpenStack Compute API v2.1
=============================================================================

Ping An Instance
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_ping_an_instance_v2.1_tenant_id_os-fping_instance_id_.rst#request>`__
`Response <GET_ping_an_instance_v2.1_tenant_id_os-fping_instance_id_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-fping/{instance_id}

Run the fping utility to ping an instance and report whether it is alive.

Policy defaults enable only users with the administrative role or the owner of the server to perform this operation. Cloud providers can change these permissions through the ``policy.json`` file.



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
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+
|{instance_id}             |csapi:UUID               |The UUID of the instance.|
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Ping An Instance: JSON request**


.. code::

    {
        "server": {
            "alive": false,
            "id": "f5e6fd6d-c0a3-4f9e-aabf-d69196b6d11a",
            "project_id": "openstack"
        }
    }
    

