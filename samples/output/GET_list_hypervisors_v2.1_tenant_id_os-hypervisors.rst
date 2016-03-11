=============================================================================
List Hypervisors -  OpenStack Compute API v2.1
=============================================================================

List Hypervisors
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_hypervisors_v2.1_tenant_id_os-hypervisors.rst#request>`__
`Response <GET_list_hypervisors_v2.1_tenant_id_os-hypervisors.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-hypervisors

Lists hypervisors.



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





**Example List Hypervisors: JSON request**


.. code::

    {
        "hypervisors": [
            {
                "status": "enabled",
                "state": "up",
                "id": 1,
                "hypervisor_hostname": "fake-mini"
            }
        ]
    }
    

