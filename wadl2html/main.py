#!/usr/bin/env python

import os
import xml.parsers.expat

filename = 'samples/cloud-images/wadl/image-2.0.wadl'

def start_resource(name,attrs):
    print('start resource: ', attrs)
def start_resources(name,attrs):
    print('start resources ', attrs)

start_dispatch = {
    'resource': start_resource,
    'resources': start_resources,
}

# handler functions
def start_element(name, attrs):
#    print('Start element:', name, attrs)
    if name in start_dispatch:
        start_dispatch[name](name, attrs)

def end_element(name):
    #print('End element:', name)
    pass
def char_data(data):
    #print('Character data:', repr(data))
    pass
def entity_data(entityName, is_parameter_entity, value, base, systemId, publicId, notationName):
    #print('Entity data:',entityName)
    pass
def default(data):
    #print('Default:', data)
    pass

p = xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data
p.EntityDeclHandler = entity_data
p.DefaultHandler = default

def main():
    with open(filename,'rb') as file:
        p.ParseFile(file)

main()
