=============================================================================
Get Detailed Availability Zone Information -  OpenStack Compute API v2.1
=============================================================================

Get Detailed Availability Zone Information
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_get_detailed_availability_zone_information_v2.1_tenant_id_os-availability-zone_detail.rst#request>`__
`Response <GET_get_detailed_availability_zone_information_v2.1_tenant_id_os-availability-zone_detail.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-availability-zone/detail

Gets detailed availability zone information.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Get detailed             |                         |
|                          |availability zone        |                         |
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





**Example Get detailed availability zone information: JSON response**


.. code::

    {
        "availabilityZoneInfo": [
            {
                "zoneState": {
                    "available": true
                },
                "hosts": {
                    "test-host": {
                        "nova-conductor": {
                            "available": true,
                            "active": true,
                            "updated_at": "2015-04-16T08:58:55.000000"
                        },
                        "nova-cert": {
                            "available": true,
                            "active": true,
                            "updated_at": "2015-04-16T08:58:55.000000"
                        },
                        "nova-consoleauth": {
                            "available": true,
                            "active": true,
                            "updated_at": "2015-04-16T08:58:55.000000"
                        },
                        "nova-scheduler": {
                            "available": true,
                            "active": true,
                            "updated_at": "2015-04-16T08:58:55.000000"
                        },
                        "nova-network": {
                            "available": true,
                            "active": true,
                            "updated_at": "2015-04-16T08:58:54.000000"
                        }
                    }
                },
                "zoneName": "internal"
            },
            {
                "zoneState": {
                    "available": true
                },
                "hosts": {
                    "test-host": {
                        "nova-compute": {
                            "available": true,
                            "active": true,
                            "updated_at": "2015-04-16T08:58:56.000000"
                        }
                    }
                },
                "zoneName": "nova"
            }
        ]
    }
    

