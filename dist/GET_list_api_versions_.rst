=============================================================================
List Api Versions -  OpenStack Compute API v2.1
=============================================================================

List Api Versions
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_api_versions_.rst#request>`__
`Response <GET_list_api_versions_.rst#response>`__

.. code-block:: javascript

    GET /

Lists information about all Networking API versions.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200 300                   |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^









Response
^^^^^^^^^^^^^^^^^^





**Example List Api Versions: JSON request**


.. code::

    {"versions": [{"status": "CURRENT","id": "v2.0","links": [{"href": "http://23.253.228.211:9696/v2.0","rel": "self"}]}]}

