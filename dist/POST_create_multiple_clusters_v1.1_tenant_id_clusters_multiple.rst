=============================================================================
Create Multiple Clusters -  OpenStack Compute API v2.1
=============================================================================

Create Multiple Clusters
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_multiple_clusters_v1.1_tenant_id_clusters_multiple.rst#request>`__
`Response <POST_create_multiple_clusters_v1.1_tenant_id_clusters_multiple.rst#response>`__

.. code-block:: javascript

    POST /v1.1/{tenant_id}/clusters/multiple

Creates multiple clusters.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|202                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









**Example Create Multiple Clusters: JSON request**


.. code::

    {"plugin_name": "vanilla","hadoop_version": "2.6.0","cluster_template_id": "9951f86d-57ba-43d6-9cb0-14ed2ec7a6cf","default_image_id": "bc3c3d3c-2684-4bf8-a9fa-388fb71288a9","user_keypair_id": "test","name": "def-cluster","count": 2,"cluster_configs": {},"neutron_management_network": "7e31648b-4b2e-4f32-9b0a-113581c27076"}


Response
^^^^^^^^^^^^^^^^^^





**Example Create Multiple Clusters: JSON request**


.. code::

    {"clusters": ["a007a3e7-658f-4568-b0f2-fe2fd5efc554","b012a6et-65hf-4566-b0f2-fe3fd7efc567"]}

