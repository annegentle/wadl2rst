
Show Console Output (Os-Getconsoleoutput Action)
================================================

`Request <POST_show_console_output_(os-getconsoleoutput_action)_v2.1_tenant_id_servers_server_id_action.rst#request>`__
`Response <POST_show_console_output_(os-getconsoleoutput_action)_v2.1_tenant_id_servers_server_id_action.rst#response>`__

.. rest_method:: POST /v2.1/{tenant_id}/servers/{server_id}/action

Shows console output for a server instance.

Specify the ``os-getConsoleOutput`` action in the request body.



Normal response codes: 200

Error response codes: computeFault(400, 500), serviceUnavailable(503), badRequest(400),
unauthorized(401), forbidden(403), badMethod(405), itemNotFound(404)

Request
^^^^^^^




.. rest_parameters:: showConsoleOutput(Os-GetconsoleoutputAction).yaml

	- os-getConsoleOutput: os-getConsoleOutput
	- length: length




**Example Get console output: JSON request**


.. code::

    {
        "os-getConsoleOutput": {
            "length": 50
        }
    }
    


Response
^^^^^^^^





**Example Get console output: JSON response**


.. code::

    {
        "output": "FAKE CONSOLE OUTPUT\nANOTHER\nLAST LINE"
    }
    

