=============================================================================
List Policies -  OpenStack Compute API v2.1
=============================================================================

List Policies
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_policies_v1_clusters_cluster_id_policies.rst#request>`__
`Response <GET_list_policies_v1_clusters_cluster_id_policies.rst#response>`__

.. code-block:: javascript

    GET /v1/clusters/{cluster_id}/policies

Lists all policies for a cluster.



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
|{cluster_id}              |csapi:UUID *(Required)*  |The UUID of the cluster. |
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+-------------------------+------------------------+---------------------------+
|Name                     |Type                    |Description                |
+=========================+========================+===========================+
|sort                     |xsd:string *(Required)* |Sorts the response by one  |
|                         |                        |or more attribute and      |
|                         |                        |optional sort direction    |
|                         |                        |combinations. A valid      |
|                         |                        |direction is ``asc``       |
|                         |                        |(ascending) or ``desc``    |
|                         |                        |(descending). Default      |
|                         |                        |direction is ``asc``       |
|                         |                        |(ascending). Specify the   |
|                         |                        |list as < key > [: <       |
|                         |                        |direction > ]. For         |
|                         |                        |example, the following     |
|                         |                        |query parameters in the    |
|                         |                        |URI sort the objects in    |
|                         |                        |the response by ``name``   |
|                         |                        |in ascending order and     |
|                         |                        |then by ``status`` in      |
|                         |                        |descending order: GET      |
|                         |                        |/v2/images?sort=name:asc,  |
|                         |                        |status:descThe following   |
|                         |                        |query parameters in the    |
|                         |                        |URI sort the objects in    |
|                         |                        |the response by ``name``   |
|                         |                        |in descending order and    |
|                         |                        |then by ``status`` in      |
|                         |                        |ascending order. GET       |
|                         |                        |/v2/images?sort=name:desc, |
|                         |                        |status                     |
+-------------------------+------------------------+---------------------------+
|enabled                  |xsd:boolean *(Required)*|Filters the response by a  |
|                         |                        |policy enabled status on   |
|                         |                        |the cluster.               |
+-------------------------+------------------------+---------------------------+







Response
^^^^^^^^^^^^^^^^^^





**Example List Policies: JSON request**


.. code::

    {"cluster_policies": [{"cluster_id": "7d85f602-a948-4a30-afd4-e84f47471c15","cluster_name": "cluster4","enabled": true,"id": "06be3a1f-b238-4a96-a737-ceec5714087e","policy_id": "714fe676-a08f-4196-b7af-61d52eeded15","policy_name": "dp01","policy_type": "senlin.policy.deletion-1.0"},{"cluster_id": "7d85f602-a948-4a30-afd4-e84f47471c15","cluster_name": "cluster4","enabled": true,"id": "abddc45e-ac31-4f90-93cc-db55a7d8dd6d","policy_id": "e026e09f-a3e9-4dad-a1b9-d7ba316026a1","policy_name": "sp1","policy_type": "senlin.policy.scaling-1.0"}]}

