=============================================================================
Create Property -  OpenStack Image API v2
=============================================================================

Create Property
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_property_v2_metadefs_namespaces_namespace_id_properties.rst#request>`__
`Response <POST_create_property_v2_metadefs_namespaces_namespace_id_properties.rst#response>`__

.. code-block:: javascript

    POST /v2/metadefs/namespaces/{namespace_id}/properties

Creates a property definition in a namespace.

The schema is a subset of the JSON property definition schema.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|201                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+





This table shows the body parameters for the request:

+----------------+------------------+-----------------------------------------------+
|Name            |Type              |Description                                    |
+================+==================+===============================================+
|name            |xsd:string        |The name of the property.                      |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|title           |xsd:string        |The title of the property.                     |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|type            |xsd:string        |The property type.                             |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|enum            |xsd:list          |Enumerated list of property values.            |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|items           |xsd:string        |Schema for the items in an array.              |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|description     |xsd:string        |The description of the property.               |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|operators       |xsd:string        |Operators property description.                |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|default         |xsd:base64Binary  |Default property description.                  |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|readonly        |xsd:boolean       |Indicates whether this is a read-only property.|
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|minimum         |xsd:string        |Minimum allowed numerical value.               |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|maximum         |xsd:string        |Maximum allowed numerical value.               |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|minLength       |xsd:string        |Minimum allowed string length.                 |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|maxLength       |xsd:string        |Maximum allowed string length.                 |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|pattern         |xsd:string        |A regular expression ( `ECMA262                |
|                |*(Required)*      |<http://www.ecma-                              |
|                |                  |international.org/publications/standards/Ecma- |
|                |                  |262.htm>`__ ) that a string value must match.  |
+----------------+------------------+-----------------------------------------------+
|minItems        |xsd:string        |Minimum length of an array.                    |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|maxItems        |xsd:string        |Maximum length of an array.                    |
|                |*(Required)*      |                                               |
+----------------+------------------+-----------------------------------------------+
|uniqueItems     |xsd:string        |Indicates whether all values in the array must |
|                |*(Required)*      |be distinct.                                   |
+----------------+------------------+-----------------------------------------------+
|additionalItems |xsd:string        |Describes extra items, if you use tuple        |
|                |*(Required)*      |typing. If the value of ``items`` is an array  |
|                |                  |(tuple typing) and the instance is longer than |
|                |                  |the list of schemas in ``items``, the          |
|                |                  |additional items are described by the schema   |
|                |                  |in this property. If this value is ``false``,  |
|                |                  |the instance cannot be longer than the list of |
|                |                  |schemas in ``items``. If this value is         |
|                |                  |``true``, that is equivalent to the empty      |
|                |                  |schema (anything goes).                        |
+----------------+------------------+-----------------------------------------------+





**Example Create Property: JSON request**


.. code::

    {
        "description": "The hypervisor type. It may be used by the host properties filter for scheduling. The ImagePropertiesFilter filters compute nodes that satisfy any architecture, hypervisor type, or virtual machine mode properties specified on the instance's image properties. Image properties are contained in the image dictionary in the request_spec.",
        "enum": [
            "xen",
            "qemu",
            "kvm",
            "lxc",
            "uml",
            "vmware",
            "hyperv"
        ],
        "name": "hypervisor_type",
        "title": "Hypervisor Type",
        "type": "string"
    }
    


Response
^^^^^^^^^^^^^^^^^^


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|name                      |xsd:string *(Required)*  |The name of the property.|
+--------------------------+-------------------------+-------------------------+
|title                     |xsd:string *(Required)*  |The title of the         |
|                          |                         |property.                |
+--------------------------+-------------------------+-------------------------+
|type                      |xsd:string *(Required)*  |The property type.       |
+--------------------------+-------------------------+-------------------------+
|enum                      |xsd:list *(Required)*    |Enumerated list of       |
|                          |                         |property values.         |
+--------------------------+-------------------------+-------------------------+
|items                     |xsd:string *(Required)*  |Schema for the items in  |
|                          |                         |an array.                |
+--------------------------+-------------------------+-------------------------+
|description               |xsd:string *(Required)*  |The description of the   |
|                          |                         |property.                |
+--------------------------+-------------------------+-------------------------+
|operators                 |xsd:string *(Required)*  |Operators property       |
|                          |                         |description.             |
+--------------------------+-------------------------+-------------------------+
|default                   |xsd:base64Binary         |Default property         |
|                          |*(Required)*             |description.             |
+--------------------------+-------------------------+-------------------------+
|readonly                  |xsd:boolean *(Required)* |Indicates whether this   |
|                          |                         |is a read-only property. |
+--------------------------+-------------------------+-------------------------+
|minimum                   |xsd:string *(Required)*  |Minimum allowed          |
|                          |                         |numerical value.         |
+--------------------------+-------------------------+-------------------------+
|maximum                   |xsd:string *(Required)*  |Maximum allowed          |
|                          |                         |numerical value.         |
+--------------------------+-------------------------+-------------------------+
|minLength                 |xsd:string *(Required)*  |Minimum allowed string   |
|                          |                         |length.                  |
+--------------------------+-------------------------+-------------------------+
|maxLength                 |xsd:string *(Required)*  |Maximum allowed string   |
|                          |                         |length.                  |
+--------------------------+-------------------------+-------------------------+
|pattern                   |xsd:string *(Required)*  |A regular expression     |
|                          |                         |(ECMA 262) that a string |
|                          |                         |value must match.        |
+--------------------------+-------------------------+-------------------------+
|minItems                  |xsd:string *(Required)*  |Minimum length of an     |
|                          |                         |array.                   |
+--------------------------+-------------------------+-------------------------+
|maxItems                  |xsd:string *(Required)*  |Maximum length of an     |
|                          |                         |array.                   |
+--------------------------+-------------------------+-------------------------+
|uniqueItems               |xsd:string *(Required)*  |Indicates whether all    |
|                          |                         |values in the array must |
|                          |                         |be distinct.             |
+--------------------------+-------------------------+-------------------------+
|additionalItems           |xsd:string *(Required)*  |Describes extra items,   |
|                          |                         |if you use tuple typing. |
|                          |                         |If the value of          |
|                          |                         |``items`` is an array    |
|                          |                         |(tuple typing) and the   |
|                          |                         |instance is longer than  |
|                          |                         |the list of schemas in   |
|                          |                         |``items``, the           |
|                          |                         |additional items are     |
|                          |                         |described by the schema  |
|                          |                         |in this property. If     |
|                          |                         |this value is ``false``, |
|                          |                         |the instance cannot be   |
|                          |                         |longer than the list of  |
|                          |                         |schemas in ``items``. If |
|                          |                         |this value is ``true``,  |
|                          |                         |that is equivalent to    |
|                          |                         |the empty schema         |
|                          |                         |(anything goes).         |
+--------------------------+-------------------------+-------------------------+





**Example Create Property: JSON request**


.. code::

    {
        "description": "The hypervisor type. It may be used by the host properties filter for scheduling. The ImagePropertiesFilter filters compute nodes that satisfy any architecture, hypervisor type, or virtual machine mode properties specified on the instance's image properties. Image properties are contained in the image dictionary in the request_spec.",
        "enum": [
            "xen",
            "qemu",
            "kvm",
            "lxc",
            "uml",
            "vmware",
            "hyperv"
        ],
        "name": "hypervisor_type",
        "title": "Hypervisor Type",
        "type": "string"
    }
    

