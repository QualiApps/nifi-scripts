#!/usr/bin/env python

from sys import exit, argv
from json import loads, dumps
from ipso import IPSO_OBJECTS as ipso
from time import time


class FilterIPSO(object):
    def __init__(self, objectId, raw_data):
	self.__data = []
	self.raw_data = raw_data
	self.process(objectId)

    def process(self, id):
	object_info = ipso.get(id)
	if object_info:
	    self.create_points(object_info)

    def create_points(self, obj):
	raw_resources = self.get_resources()
	for resource in raw_resources:
	    if resource['id'] in obj['required']:
		res_attribs = self.get_obj_attr(resource['id'], obj['attrib'])
		tags = {
		    "endpoint": self.raw_data.get('endpoint'),
		    "object_id": self.raw_data.get('objectId'),
		    "instance_id": self.raw_data.get('objectInstanceId'),
		    "resource_id": resource['id'],
		    "resource_title": self.convert_name(res_attribs['description'])
		}
		values = {
		    "value": resource.get('value', 0)
		}
		point = self.format_to_line(
			    self.convert_name(obj.get('title')), 
			    tags,
			    values,
			    int(time())
			)

		self.__data.append(point)
    
    @staticmethod
    def get_obj_attr(res_id, attrib):
	response = None
	for attr in attrib:
	    if int(attr['id']) == res_id:
		response = attr
		break

	return response
	

    def format_to_line(self, measurement, tags, values, timestamp):
	return '%s%s %s %s' % (measurement, ',' + self.dict_to_line(tags) if tags else '', self.dict_to_line(values), timestamp)

    @staticmethod
    def dict_to_line(items):
	return ','.join(['%s=%s' % (k,v) for k,v in items.iteritems()])

    @staticmethod
    def convert_name(name):
	return name.lower().replace(" ", "_")

    def get_resources(self):
	return self.raw_data.get('content').get('resources')

    @property
    def data(self):
	return "\n".join(self.__data)

    def __str__(self):
	return self.data


if __name__ == '__main__':
    if len(argv) == 2:
	input_data = raw_input()
        print FilterIPSO(int(argv[1]), loads(input_data))

exit(0)
