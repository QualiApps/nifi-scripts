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
		point = {
		    "measurement": obj.get('title'),
		    "tags": {
			"endpoint": self.raw_data.get('endpoint'),
			"objectId": self.raw_data.get('objectId'),
			"instanceId": self.raw_data.get('objectInstanceId')
		    },
		    "time": str(time()),
		    "fields": {
			"value": resource['value']
		    }
		}
		self.__data.append(point)

    def get_resources(self):
	return self.raw_data.get('content').get('resources')

    @property
    def data(self):
	return dumps(self.__data)

    def __str__(self):
	return self.data


if __name__ == '__main__':
    if len(argv) == 2:
	input_data = raw_input()
        print FilterIPSO(int(argv[1]), loads(input_data))

exit(0)
