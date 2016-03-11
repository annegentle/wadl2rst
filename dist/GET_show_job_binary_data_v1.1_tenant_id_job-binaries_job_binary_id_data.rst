=============================================================================
Show Job Binary Data -  OpenStack Compute API v2.1
=============================================================================

Show Job Binary Data
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_job_binary_data_v1.1_tenant_id_job-binaries_job_binary_id_data.rst#request>`__
`Response <GET_show_job_binary_data_v1.1_tenant_id_job-binaries_job_binary_id_data.rst#response>`__

.. code-block:: javascript

    GET /v1.1/{tenant_id}/job-binaries/{job_binary_id}/data

Shows data for a job binary.

The response body shows the job binary raw data and the response headers show the data length.

Example response:

HTTP/1.1 200 OKConnection: keep-aliveContent-Length: 161Content-Type: text/html; charset=utf-8Date: Sat, 28 Mar 2016 02:42:48 GMTA = load '$INPUT' using PigStorage(':') as (fruit: chararray);B = foreach A generate com.hadoopbook.pig.Trim(fruit);store B into '$OUTPUT' USING PigStorage();

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
|{job_binary_id}           |capi:UUID                |The UUID of the job      |
|                          |                         |binary.                  |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




