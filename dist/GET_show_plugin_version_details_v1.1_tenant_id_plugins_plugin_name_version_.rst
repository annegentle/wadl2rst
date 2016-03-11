=============================================================================
Show Plugin Version Details -  OpenStack Compute API v2.1
=============================================================================

Show Plugin Version Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_plugin_version_details_v1.1_tenant_id_plugins_plugin_name_version_.rst#request>`__
`Response <GET_show_plugin_version_details_v1.1_tenant_id_plugins_plugin_name_version_.rst#response>`__

.. code-block:: javascript

    GET /v1.1/{tenant_id}/plugins/{plugin_name}/{version}

Shows details for a plugin version.



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
|{version}                 |xsd:string               |Version of the plugin.   |
+--------------------------+-------------------------+-------------------------+
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





**Example Show Plugin Version Details: JSON request**


.. code::

    {"plugin": {"name": "vanilla","versions": ["1.2.1","2.4.1","2.6.0"],"description": "The Apache Vanilla plugin provides the ability to launch upstream Vanilla Apache Hadoop cluster without any management consoles. It can also deploy the Oozie component.","required_image_tags": ["vanilla","2.6.0"],"node_processes": {"JobFlow": ["oozie"],"HDFS": ["namenode","datanode","secondarynamenode"],"YARN": ["resourcemanager","nodemanager"],"MapReduce": ["historyserver"],"Hadoop": [],"Hive": ["hiveserver"]},"configs": [{"default_value": "/tmp/hadoop-${user.name}","name": "hadoop.tmp.dir","priority": 2,"config_type": "string","applicable_target": "HDFS","is_optional": true,"scope": "node","description": "A base for other temporary directories."},{"default_value": true,"name": "hadoop.native.lib","priority": 2,"config_type": "bool","applicable_target": "HDFS","is_optional": true,"scope": "node","description": "Should native hadoop libraries, if present, be used."},{"default_value": 1024,"name": "NodeManager Heap Size","config_values": null,"priority": 1,"config_type": "int","applicable_target": "YARN","is_optional": false,"scope": "node","description": null},{"default_value": true,"name": "Enable Swift","config_values": null,"priority": 1,"config_type": "bool","applicable_target": "general","is_optional": false,"scope": "cluster","description": null},{"default_value": true,"name": "Enable MySQL","config_values": null,"priority": 1,"config_type": "bool","applicable_target": "general","is_optional": true,"scope": "cluster","description": null}],"title": "Vanilla Apache Hadoop"}}

