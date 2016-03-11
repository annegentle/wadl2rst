=============================================================================
Show Plugin Details -  OpenStack Compute API v2.1
=============================================================================

Show Plugin Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_plugin_details_v1.1_tenant_id_plugins_plugin_name_.rst#request>`__
`Response <GET_show_plugin_details_v1.1_tenant_id_plugins_plugin_name_.rst#response>`__

.. code-block:: javascript

    GET /v1.1/{tenant_id}/plugins/{plugin_name}

Shows details for a plugin.



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
|{plugin_name}             |xsd:string               |Name of the plugin.      |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The name of the plugin.  |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The full description of  |
|                          |                         |the plugin.              |
+--------------------------+-------------------------+-------------------------+
|versions                  |xsd:list *(Required)*    |The list of plugin       |
|                          |                         |versions.                |
+--------------------------+-------------------------+-------------------------+
|title                     |xsd:string *(Required)*  |The title of the plugin. |
+--------------------------+-------------------------+-------------------------+





**Example Show Plugin Details: JSON request**


.. code::

    {"plugin": {"name": "vanilla","versions": ["1.2.1","2.4.1","2.6.0"],"title": "Vanilla Apache Hadoop","description": "The Apache Vanilla plugin provides the ability to launch upstream Vanilla Apache Hadoop cluster without any management consoles. It can also deploy the Oozie component."}}

