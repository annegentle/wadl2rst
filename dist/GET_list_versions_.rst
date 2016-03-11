=============================================================================
List Versions -  OpenStack Compute API v2.1
=============================================================================

List Versions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_versions_.rst#request>`__
`Response <GET_list_versions_.rst#response>`__

.. code-block:: javascript

    GET /

Lists information for all Clustering API versions.



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





**Example List Versions: JSON request**


.. code::

    {"versions": [{"status": "CURRENT","id": "v1.0","links": [{"href": "http://192.168.12.34:8778/v1/","rel": "self"}]}]}

