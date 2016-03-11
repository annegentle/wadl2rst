=============================================================================
Show Build Information -  OpenStack Compute API v2.1
=============================================================================

Show Build Information
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_build_information_v1_build-info.rst#request>`__
`Response <GET_show_build_information_v1_build-info.rst#response>`__

.. code-block:: javascript

    GET /v1/build-info

Shows build information for a Senlin deployment.



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





**Example Show Build Information: JSON request**


.. code::

    {"build_info": {"api": {"revision": "1.0"},"engine": {"revision": "2.0"}}}

