=============================================================================
List Job Binaries -  OpenStack Compute API v2.1
=============================================================================

List Job Binaries
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_job_binaries_v1.1_tenant_id_job-binaries.rst#request>`__
`Response <GET_list_job_binaries_v1.1_tenant_id_job-binaries.rst#response>`__

.. code-block:: javascript

    GET /v1.1/{tenant_id}/job-binaries

Lists the available job binaries.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+----------------+---------------+---------------------------------------------+
|Name            |Type           |Description                                  |
+================+===============+=============================================+
|binaries        |xsd:list       |The list of job binary internal objects.     |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|description     |xsd:string     |The description of the job binary object.    |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|url             |xsd:string     |The url of the job binary object.            |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|is_public       |xsd:boolean    |If set to ``true``, the object is public.    |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|tenant_id       |csapi:UUID     |The UUID of the tenant.                      |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|is_protected    |xsd:boolean    |If set to ``true``, the object is protected. |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|created_at      |xsd:dateTime   |The date and time when the object was        |
|                |*(Required)*   |created. The date and time stamp format is   |
|                |               |`ISO 8601                                    |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+
|id              |csapi:UUID     |The ID of the object.                        |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+
|updated_at      |xsd:dateTime   |The date and time when the object was        |
|                |*(Required)*   |updated. The date and time stamp format is   |
|                |               |`ISO 8601                                    |
|                |               |<https://en.wikipedia.org/wiki/ISO_8601>`__  |
|                |               |: CCYY-MM-DDThh:mm:ss±hh:mmThe ``±hh:mm``    |
|                |               |value, if included, returns the time zone as |
|                |               |an offset from UTC. For example, ``2015-08-  |
|                |               |27T09:49:58-05:00``.                         |
+----------------+---------------+---------------------------------------------+
|name            |xsd:string     |The name of the object.                      |
|                |*(Required)*   |                                             |
+----------------+---------------+---------------------------------------------+





**Example List Job Binaries: JSON request**


.. code::

    {"binaries": [{"is_public": false,"description": "","url": "internal-db://d2498cbf-4589-484a-a814-81436c18beb3","tenant_id": "11587919cc534bcbb1027a161c82cf58","created_at": "2013-10-15 12:36:59.375060","updated_at": null,"id": "84248975-3c82-4206-a58d-6e7fb3a563fd","name": "example.pig","is_protected": false},{"is_public": false,"description": "","url": "internal-db://22f1d87a-23c8-483e-a0dd-cb4a16dde5f9","tenant_id": "11587919cc534bcbb1027a161c82cf58","created_at": "2013-10-15 12:43:52.265899","updated_at": null,"id": "508fc62d-1d58-4412-b603-bdab307bb926","name": "udf.jar","is_protected": false},{"is_public": false,"description": "","url": "swift://container/jar-example.jar","tenant_id": "11587919cc534bcbb1027a161c82cf58","created_at": "2013-10-15 14:25:04.970513","updated_at": null,"id": "a716a9cd-9add-4b12-b1b6-cdb71aaef350","name": "jar-example.jar","is_protected": false}]}

