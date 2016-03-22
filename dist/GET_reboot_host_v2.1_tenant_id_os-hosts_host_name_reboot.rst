=============================================================================
Reboot Host -  OpenStack Compute API v2.1
=============================================================================

Reboot Host
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_reboot_host_v2.1_tenant_id_os-hosts_host_name_reboot.rst#request>`__
`Response <GET_reboot_host_v2.1_tenant_id_os-hosts_host_name_reboot.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-hosts/{host_name}/reboot

Reboots a host.



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





**Example Reboot Host: JSON request**


.. code::

    {
        "host": "9557750dbc464741a89c907921c1cb31",
        "power_action": "reboot"
    }
    

