=============================================================================
List Usage Audits Before Specified Time -  OpenStack Compute API v2.1
=============================================================================

List Usage Audits Before Specified Time
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_usage_audits_before_specified_time_v2.1_tenant_id_os-instance_usage_audit_log_before_timestamp_.rst#request>`__
`Response <GET_list_usage_audits_before_specified_time_v2.1_tenant_id_os-instance_usage_audit_log_before_timestamp_.rst#response>`__

.. code-block:: javascript

    GET /v2.1/{tenant_id}/os-instance_usage_audit_log/{before_timestamp}

Lists usage audits that occurred before a specified time.



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



This table shows the query parameters for the request:

+-----------------+--------------+---------------------------------------------+
|Name             |Type          |Description                                  |
+=================+==============+=============================================+
|before_timestamp |xsd:dateTime  |Filters the response by the date and time    |
|                 |*(Required)*  |before which to list usage audits. The date  |
|                 |              |and time stamp format is `ISO 8601           |
|                 |              |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                 |              |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                 |              |value, if included, returns the time zone as |
|                 |              |an offset from UTC. For example, ``2015-08-  |
|                 |              |27T09:49:58-05:00``. If you omit the time    |
|                 |              |zone, the UTC time zone is assumed.          |
+-----------------+--------------+---------------------------------------------+







Response
^^^^^^^^^^^^^^^^^^





**Example List Usage Audits Before Specified Time: JSON request**


.. code::

    {
        "instance_usage_audit_log": {
            "hosts_not_run": [
                "8e33da2b48684ef3ab165444d6a7384c"
            ],
            "log": {},
            "num_hosts": 1,
            "num_hosts_done": 0,
            "num_hosts_not_run": 1,
            "num_hosts_running": 0,
            "overall_status": "0 of 1 hosts done. 0 errors.",
            "period_beginning": "2012-06-01 00:00:00",
            "period_ending": "2012-07-01 00:00:00",
            "total_errors": 0,
            "total_instances": 0
        }
    }
    

