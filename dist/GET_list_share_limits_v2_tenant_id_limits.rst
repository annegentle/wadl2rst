=============================================================================
List Share Limits -  OpenStack Compute API v2.1
=============================================================================

List Share Limits
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_share_limits_v2_tenant_id_limits.rst#request>`__
`Response <GET_list_share_limits_v2_tenant_id_limits.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/limits

Lists share limits.



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
|X-Openstack-Manila-Api-   |xsd:string               |The HTTP header to       |
|Version                   |                         |specify a valid Shared   |
|                          |                         |File Systems API micro-  |
|                          |                         |version. For example,    |
|                          |                         |``"X-Openstack-Manila-   |
|                          |                         |Api-Version: 2.6"``. If  |
|                          |                         |you omit this header,    |
|                          |                         |the default micro-       |
|                          |                         |version is 2.0.          |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------+---------------------------------------------+
|Name                      |Type         |Description                                  |
+==========================+=============+=============================================+
|maxTotalShareGigabytes    |xsd:int      |The total maximum number of share gigabytes  |
|                          |*(Required)* |that are allowed in a project. You cannot    |
|                          |             |request a share that exceeds the allowed     |
|                          |             |gigabytes quota.                             |
+--------------------------+-------------+---------------------------------------------+
|maxTotalSnapshotGigabytes |xsd:int      |The total maximum number of snapshot         |
|                          |*(Required)* |gigabytes that are allowed in a project.     |
+--------------------------+-------------+---------------------------------------------+
|maxTotalShares            |xsd:int      |The total maximum number of shares that are  |
|                          |*(Required)* |allowed in a project.                        |
+--------------------------+-------------+---------------------------------------------+
|maxTotalShareSnapshots    |xsd:int      |The total maximum number of share snapshots  |
|                          |*(Required)* |that are allowed in a project.               |
+--------------------------+-------------+---------------------------------------------+
|maxTotalShareNetworks     |xsd:int      |The total maximum number of share-networks   |
|                          |*(Required)* |that are allowed in a project.               |
+--------------------------+-------------+---------------------------------------------+
|totalSharesUsed           |xsd:int      |The total number of created shares in a      |
|                          |*(Required)* |project.                                     |
+--------------------------+-------------+---------------------------------------------+
|totalShareSnapshotsUsed   |xsd:int      |The total number of created share snapshots  |
|                          |*(Required)* |in a project.                                |
+--------------------------+-------------+---------------------------------------------+
|totalShareNetworksUsed    |xsd:int      |The total number of created share-networks   |
|                          |*(Required)* |in a project.                                |
+--------------------------+-------------+---------------------------------------------+
|totalShareGigabytesUsed   |xsd:int      |The total number of gigabytes used in a      |
|                          |*(Required)* |project by shares.                           |
+--------------------------+-------------+---------------------------------------------+
|totalSnapshotGigabytesUsed|xsd:int      |The total number of gigabytes used in a      |
|                          |*(Required)* |project by snapshots.                        |
+--------------------------+-------------+---------------------------------------------+
|uri                       |xsd:anyURI   |A human-readable URI of a rate limit.        |
+--------------------------+-------------+---------------------------------------------+
|regex                     |xsd:string   |An API regular expression. For example,      |
|                          |             |``^/shares`` for the ``/shares`` API URI or  |
|                          |             |``.*`` for any URI.                          |
+--------------------------+-------------+---------------------------------------------+
|value                     |xsd:int      |The number of API requests that are allowed  |
|                          |             |during a time interval. Used in conjunction  |
|                          |             |with the ``unit`` parameter, expressed as    |
|                          |             |``value`` per ``unit``. For example, 120     |
|                          |             |requests are allowed per minute.             |
+--------------------------+-------------+---------------------------------------------+
|verb                      |xsd:string   |The HTTP method for the API request. For     |
|                          |             |example, ``GET``, ``POST``, ``DELETE``, and  |
|                          |             |so on.                                       |
+--------------------------+-------------+---------------------------------------------+
|remaining                 |xsd:int      |The remaining number of allowed requests.    |
+--------------------------+-------------+---------------------------------------------+
|unit                      |xsd:string   |The time interval during which a number of   |
|                          |             |API requests are allowed. A valid value is   |
|                          |             |``SECOND``, ``MINUTE``, ``HOUR``, or         |
|                          |             |``DAY``. Used in conjunction with the        |
|                          |             |``value`` parameter, expressed as ``value``  |
|                          |             |per ``unit``. For example, 120 requests are  |
|                          |             |allowed per minute.                          |
+--------------------------+-------------+---------------------------------------------+
|next-available            |xsd:dateTime |The date and time stamp when next issues are |
|                          |             |available. The date and time stamp format is |
|                          |             |`ISO 8601                                    |
|                          |             |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                          |             |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                          |             |value, if included, returns the time zone as |
|                          |             |an offset from UTC. For example, ``2015-08-  |
|                          |             |27T09:49:58-05:00``.                         |
+--------------------------+-------------+---------------------------------------------+





**Example List Share Limits: JSON request**


.. code::

    {"limits": {"rate": [],"absolute": {"totalShareNetworksUsed": 0,"maxTotalShareGigabytes": 1000,"maxTotalShareNetworks": 10,"totalSharesUsed": 0,"totalShareGigabytesUsed": 0,"totalShareSnapshotsUsed": 0,"maxTotalShares": 50,"totalSnapshotGigabytesUsed": 0,"maxTotalSnapshotGigabytes": 1000,"maxTotalShareSnapshots": 50}}}

