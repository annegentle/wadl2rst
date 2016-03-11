=============================================================================
List Plugins -  OpenStack Compute API v2.1
=============================================================================

List Plugins
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_plugins_v1.1_tenant_id_plugins.rst#request>`__
`Response <GET_list_plugins_v1.1_tenant_id_plugins.rst#response>`__

.. code-block:: javascript

    GET /v1.1/{tenant_id}/plugins

Lists all registered plugins.



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

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|plugins                   |xsd:list *(Required)*    |The list of plugins.     |
+--------------------------+-------------------------+-------------------------+
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





**Example List Plugins: JSON request**


.. code::

    {"plugins": [{"name": "vanilla","description": "The Apache Vanilla plugin provides the ability to launch upstream Vanilla Apache Hadoop cluster without any management consoles. It can also deploy the Oozie component.","versions": ["1.2.1","2.4.1","2.6.0"],"title": "Vanilla Apache Hadoop"},{"name": "hdp","description": "The Hortonworks Sahara plugin automates the deployment of the Hortonworks Data Platform (HDP) on OpenStack.","versions": ["1.3.2","2.0.6"],"title": "Hortonworks Data Platform"},{"name": "spark","description": "This plugin provides an ability to launch Spark on Hadoop CDH cluster without any management consoles.","versions": ["1.0.0","0.9.1"],"title": "Apache Spark"},{"name": "cdh","description": "The Cloudera Sahara plugin provides the ability to launch the Cloudera distribution of Apache Hadoop (CDH) with Cloudera Manager management console.","versions": ["5","5.3.0"],"title": "Cloudera Plugin"}]}

