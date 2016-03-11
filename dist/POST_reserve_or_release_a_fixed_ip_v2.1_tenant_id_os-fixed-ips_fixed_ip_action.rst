=============================================================================
Reserve Or Release A Fixed Ip -  OpenStack Compute API v2.1
=============================================================================

Reserve Or Release A Fixed Ip
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_reserve_or_release_a_fixed_ip_v2.1_tenant_id_os-fixed-ips_fixed_ip_action.rst#request>`__
`Response <POST_reserve_or_release_a_fixed_ip_v2.1_tenant_id_os-fixed-ips_fixed_ip_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/os-fixed-ips/{fixed_ip}/action

Reserves or releases a fixed IP.

To reserve a fixed IP address, specify ``reserve`` in the request body. To release a fixed IP address, specify ``unreserve`` in the request body.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|415                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{fixed_ip}                |xsd:string *(Required)*  |The fixed IP of interest |
|                          |                         |to you.                  |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+








**Example Reserve Or Release A Fixed Ip: JSON request**


.. code::

    {"reserve": null}


Response
^^^^^^^^^^^^^^^^^^




