=============================================================================
Get Availability Zone Information -  OpenStack Compute API v2.1
=============================================================================

Get Availability Zone Information
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_get_availability_zone_information_v2.1_tenant_id_os-availability-zone.rst#request>`__
`Response <GET_get_availability_zone_information_v2.1_tenant_id_os-availability-zone.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-availability-zone

Gets availability zone information.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Get availability zone    |                         |
|                          |information: JSON        |                         |
|                          |response                 |                         |
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





**Example Get availability zone information: JSON response**


.. code::

    {
        "availabilityZoneInfo": [
            {
                "zoneState": {
                    "available": true
                },
                "hosts": null,
                "zoneName": "nova"
            }
        ]
    }
    

