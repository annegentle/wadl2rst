=============================================================================
Create Cluster -  OpenStack Compute API v2.1
=============================================================================

Create Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_cluster_v1.1_tenant_id_clusters.rst#request>`__
`Response <POST_create_cluster_v1.1_tenant_id_clusters.rst#response>`__

.. code-block:: javascript

    POST /v1.1/{tenant_id}/clusters

Creates a cluster.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









**Example Create cluster: JSON request**


.. code::

    {"plugin_name": "vanilla","hadoop_version": "2.7.1","cluster_template_id": "57c92a7c-5c6a-42ea-9c6f-9f40a5aa4b36","default_image_id": "4118a476-dfdc-4b0e-8d5c-463cba08e9ae","user_keypair_id": "test","name": "vanilla-cluster","neutron_management_network": "b1610452-2933-46b0-bf31-660cfa5621bd"}


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+---------------------------+-------------------------+------------------------+
|Name                       |Type                     |Description             |
+===========================+=========================+========================+
|status_description         |xsd:string *(Required)*  |The description of the  |
|                           |                         |cluster status.         |
+---------------------------+-------------------------+------------------------+
|neutron_management_network |csapi:UUID *(Required)*  |The UUID of the neutron |
|                           |                         |management network.     |
+---------------------------+-------------------------+------------------------+
|management_public_key      |xsd:string *(Required)*  |The SSH key for the     |
|                           |                         |management network.     |
+---------------------------+-------------------------+------------------------+
|cluster_template_id        |csapi:UUID *(Required)*  |The UUID of the cluster |
|                           |                         |template.               |
+---------------------------+-------------------------+------------------------+
|count                      |xsd:int *(Required)*     |The number of nodes in  |
|                           |                         |the cluster.            |
+---------------------------+-------------------------+------------------------+
|info                       |xsd:dict *(Required)*    |A set of key and value  |
|                           |                         |pairs that contain      |
|                           |                         |cluster information.    |
+---------------------------+-------------------------+------------------------+
|provision_progress         |xsd:list *(Required)*    |A list of the cluster   |
|                           |                         |progresses.             |
+---------------------------+-------------------------+------------------------+
|trust_id                   |xsd:int *(Required)*     |The id of the trust.    |
+---------------------------+-------------------------+------------------------+
|is_transient               |xsd:boolean *(Required)* |If set to ``true``, the |
|                           |                         |cluster is transient.   |
+---------------------------+-------------------------+------------------------+
|status                     |xsd:string *(Required)*  |The status of the       |
|                           |                         |cluster.                |
+---------------------------+-------------------------+------------------------+





**Example Create Cluster: JSON request**


.. code::

    {"cluster": {"is_public": false,"tenant_id": "808d5032ea0446889097723bfc8e919d","shares": null,"status_description": "","plugin_name": "vanilla","neutron_management_network": "b1610452-2933-46b0-bf31-660cfa5621bd","info": {},"user_keypair_id": "test","management_public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCfe9ARO+t9CybtuC1+cusDTeQL7wos1+U2dKPlCUJvNUn0PcunGefqWI4MUZPY9yGmvRqfINy7/xRQCzL0AwgqzwcCXamcK8JCC80uH7j8Vxa4kJheG1jxMoz/FpDSdRnzNZ+m7H5rjOwAQANhL7KatGLyCPQg9fqOoaIyCZE/A3fztm/XjJMpWnuANpUZubZtISEfu4UZKVk/DPSlBrbTZkTOvEog1LwZCZoTt0rq6a7PJFzJJkq0YecRudu/f3tpXbNe/F84sd9PhOSqcrRbm72WzglyEE8PuS1kuWpEz8G+Y5/0tQxnoh6khj9mgflrdCFuvpdutFLH4eN5MFDh Generated-by-Sahara\n","id": "e172d86c-906d-418e-a29c-6189f53bfa42","cluster_template_id": "57c92a7c-5c6a-42ea-9c6f-9f40a5aa4b36","node_groups": [{"image_id": null,"shares": null,"floating_ip_pool": "033debed-aeb8-488c-b7d0-adb74c61faa5","node_configs": {"YARN": {"yarn.nodemanager.vmem-check-enabled": "false","yarn.scheduler.maximum-allocation-mb": 2048,"yarn.scheduler.minimum-allocation-mb": 256,"yarn.nodemanager.resource.memory-mb": 2048},"MapReduce": {"yarn.app.mapreduce.am.resource.mb": 256,"mapreduce.task.io.sort.mb": 102,"mapreduce.reduce.java.opts": "-Xmx409m","mapreduce.reduce.memory.mb": 512,"mapreduce.map.memory.mb": 256,"yarn.app.mapreduce.am.command-opts": "-Xmx204m","mapreduce.map.java.opts": "-Xmx204m"}},"auto_security_group": false,"availability_zone": null,"count": 1,"flavor_id": "2","id": "0fe07f2a-0275-4bc0-93b2-c3c1e48e2815","security_groups": null,"use_autoconfig": true,"instances": [],"volumes_availability_zone": null,"created_at": "2015-09-14T10:57:11","node_group_template_id": "0bb9f1a4-0c44-4dc5-9452-6741c62ed9ae","updated_at": "2015-09-14T10:57:12","volumes_per_node": 0,"is_proxy_gateway": false,"name": "master","volume_mount_prefix": "/volumes/disk","node_processes": ["namenode","resourcemanager","oozie","historyserver"],"volumes_size": 0,"volume_local_to_instance": false,"volume_type": null},{"image_id": null,"shares": null,"floating_ip_pool": "033debed-aeb8-488c-b7d0-adb74c61faa5","node_configs": {"YARN": {"yarn.nodemanager.vmem-check-enabled": "false","yarn.scheduler.maximum-allocation-mb": 2048,"yarn.scheduler.minimum-allocation-mb": 256,"yarn.nodemanager.resource.memory-mb": 2048},"MapReduce": {"yarn.app.mapreduce.am.resource.mb": 256,"mapreduce.task.io.sort.mb": 102,"mapreduce.reduce.java.opts": "-Xmx409m","mapreduce.reduce.memory.mb": 512,"mapreduce.map.memory.mb": 256,"yarn.app.mapreduce.am.command-opts": "-Xmx204m","mapreduce.map.java.opts": "-Xmx204m"}},"auto_security_group": false,"availability_zone": null,"count": 3,"flavor_id": "2","id": "c7a3bea4-c898-446b-8c67-6d378d4c06c4","security_groups": null,"use_autoconfig": true,"instances": [],"volumes_availability_zone": null,"created_at": "2015-09-14T10:57:11","node_group_template_id": "846edb31-add5-46e6-a4ee-a4c339f99251","updated_at": "2015-09-14T10:57:12","volumes_per_node": 0,"is_proxy_gateway": false,"name": "worker","volume_mount_prefix": "/volumes/disk","node_processes": ["datanode","nodemanager"],"volumes_size": 0,"volume_local_to_instance": false,"volume_type": null}],"provision_progress": [],"hadoop_version": "2.7.1","use_autoconfig": true,"trust_id": null,"description": null,"created_at": "2015-09-14T10:57:11","is_protected": false,"updated_at": "2015-09-14T10:57:12","is_transient": false,"cluster_configs": {"HDFS": {"dfs.replication": 3}},"anti_affinity": [],"name": "vanilla-cluster","default_image_id": "4118a476-dfdc-4b0e-8d5c-463cba08e9ae","status": "Validating"}}

