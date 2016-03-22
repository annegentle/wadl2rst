=============================================================================
Shut Down Host -  OpenStack Compute API v2.1
=============================================================================

Shut Down Host
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_shut_down_host_v2.1_tenant_id_os-hosts_host_name_shutdown.rst#request>`__
`Response <GET_shut_down_host_v2.1_tenant_id_os-hosts_host_name_shutdown.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-hosts/{host_name}/shutdown

Shuts down a host.



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
|{host_name}               |xsd:string               |The name of the host.    |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Shut Down Host: JSON request**


.. code::

    {
        "host": "77cfa0002e4d45fe97f185968111b27b",
        "power_action": "shutdown"
    }
    

