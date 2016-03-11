=============================================================================
List Servers -  OpenStack Compute API v2.1
=============================================================================

List Servers
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_servers_v2_tenant_id_servers_detail.rst#request>`__
`Response <GET_list_servers_v2_tenant_id_servers_detail.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/servers/detail

Lists servers with detailed config drive information.



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








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-disk-config:diskConfig |xsd:string               |Valid value is ``AUTO``  |
|                          |                         |or ``MANUAL``.           |
+--------------------------+-------------------------+-------------------------+





**Example List Servers: JSON request**


.. code::

    

