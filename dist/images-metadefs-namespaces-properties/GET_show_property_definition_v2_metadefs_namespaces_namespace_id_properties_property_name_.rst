=============================================================================
Show Property Definition -  OpenStack Image API v2
=============================================================================

Show Property Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_property_definition_v2_metadefs_namespaces_namespace_id_properties_property_name_.rst#request>`__
`Response <GET_show_property_definition_v2_metadefs_namespaces_namespace_id_properties_property_name_.rst#response>`__

.. code-block:: javascript

    GET /v2/metadefs/namespaces/{namespace_id}/properties/{property_name}

Shows the definition for a property.

If you use the ``resource_type`` query parameter, the API removes the prefix of the resource type from the property name before it submits the query. This enables you to look for a property name that starts with a prefix from an associated resource type.

The response body shows a single property entity.



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
|{namespace_id}            |csapi:UUID               |The UUID of the          |
|                          |                         |namespace.               |
+--------------------------+-------------------------+-------------------------+
|{property_name}           |xsd:string               |The name of the property.|
+--------------------------+-------------------------+-------------------------+



This table shows the query parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|resource_type             |xsd:int *(Required)*     |Filters the response by  |
|                          |                         |property names that      |
|                          |                         |start with a prefix from |
|                          |                         |an associated resource   |
|                          |                         |type. The API removes    |
|                          |                         |the prefix of the        |
|                          |                         |resource type from the   |
|                          |                         |property name in the     |
|                          |                         |response.                |
+--------------------------+-------------------------+-------------------------+




This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|property_name             |xsd:string *(Required)*  |The name of the property.|
+--------------------------+-------------------------+-------------------------+





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





**Example Show Property Definition: JSON request**


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
    

