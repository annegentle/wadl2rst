=============================================================================
Enable Host -  OpenStack Compute API v2.1
=============================================================================

Enable Host
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_enable_host_v2.1_tenant_id_os-hosts_host_name_.rst#request>`__
`Response <PUT_enable_host_v2.1_tenant_id_os-hosts_host_name_.rst#response>`__

.. code-block:: javascript

    PUT /v2.1/{tenant_id}/os-hosts/{host_name}

Enables or puts a host in maintenance mode.



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








**Example Enable Host: JSON request**


.. code::

    {
        "status": "enable",
        "maintenance_mode": "disable"
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Enable Host: JSON request**


.. code::

    {
        "host": "65c5d5b7e3bd44308e67fc50f362aee6",
        "maintenance_mode": "off_maintenance",
        "status": "enabled"
    }
    

