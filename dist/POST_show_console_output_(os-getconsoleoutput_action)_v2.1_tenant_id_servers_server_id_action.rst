=============================================================================
Show Console Output (Os-Getconsoleoutput Action) -  OpenStack Compute API v2.1
=============================================================================

Show Console Output (Os-Getconsoleoutput Action)
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_show_console_output_(os-getconsoleoutput_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_show_console_output_(os-getconsoleoutput_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. code-block:: javascript

    POST /v2.1/{tenant_id}/servers/{server_id}/action

Shows console output for a server instance.

Specify the ``os-getConsoleOutput`` action in the request body.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Get console output: JSON |                         |
|                          |response                 |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{server_id}               |csapi:UUID               |The UUID of the server.  |
+--------------------------+-------------------------+-------------------------+
|{tenant_id}               |csapi:UUID               |The UUID of the tenant   |
|                          |                         |in a multi-tenancy cloud.|
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|os-getConsoleOutput       |xsd:string *(Required)*  |The action.              |
+--------------------------+-------------------------+-------------------------+
|length                    |                         |The number of lines to   |
|                          |                         |fetch from the end of    |
|                          |                         |console log. ``-1``      |
|                          |                         |indicates unlimited.     |
+--------------------------+-------------------------+-------------------------+





**Example Get console output: JSON request**


.. code::

    {"os-getConsoleOutput": {"length": 50}}


Response
^^^^^^^^^^^^^^^^^^





**Example Get console output: JSON response**


.. code::

    {"output": "FAKE CONSOLE OUTPUT\nANOTHER\nLAST LINE"}

