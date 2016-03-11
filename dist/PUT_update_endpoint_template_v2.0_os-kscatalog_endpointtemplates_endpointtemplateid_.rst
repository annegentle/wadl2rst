=============================================================================
Update Endpoint Template -  OpenStack Compute API v2.1
=============================================================================

Update Endpoint Template
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_endpoint_template_v2.0_os-kscatalog_endpointtemplates_endpointtemplateid_.rst#request>`__
`Response <PUT_update_endpoint_template_v2.0_os-kscatalog_endpointtemplates_endpointtemplateid_.rst#response>`__

.. code-block:: javascript

    PUT /v2.0/OS-KSCATALOG/endpointTemplates/{endpointTemplateId}

Updates endpoint template.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|401                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|403                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|405                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|413                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|415                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|503                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{endpointTemplateId}      |xsd:string               |The endpoint template ID.|
+--------------------------+-------------------------+-------------------------+
|X-Auth-Token              |xsd:string *(Required)*  |A valid authentication   |
|                          |                         |token for an             |
|                          |                         |administrative user.     |
+--------------------------+-------------------------+-------------------------+








**Example Update Endpoint Template: JSON request**


.. code::

    {"OS-KSCATALOG:endpointTemplate": {"id": 1,"region": "North","global": true,"type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","versionId": "1","versionInfo": "https://compute.north.public.com/v1/","versionList": "https://compute.north.public.com/","enabled": true}}


Response
^^^^^^^^^^^^^^^^^^





**Example Update Endpoint Template: JSON request**


.. code::

    {"OS-KSCATALOG:endpointTemplate": {"id": 1,"region": "North","global": true,"type": "compute","publicURL": "https://compute.north.public.com/v1","internalURL": "https://compute.north.internal.com/v1","enabled": true}}

