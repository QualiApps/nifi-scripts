#!/usr/bin/env python

from json import loads, dumps
from requests import get, codes
from os import sep
from urlparse import urlunparse

class LeshanPoller(object):
    __slots__ = ["_LeshanPoller__data"]

    scheme = "http"
    api_url = "api/clients"

    def __init__(self):
	self.__data = []
	self.get_data()

    def get_urls(self, input):
	"""
	    Retrieves Leshan url
	"""
	url = []
	service = loads(input)
	
	parts = (self.scheme, ":".join((service["ServiceAddress"], str(service['ServicePort']))), self.api_url, "", "", "")
	url.append(urlunparse(parts))
	
	return url

    def get_data(self):
	urls = self.get_urls(raw_input())
        leshan_instances = self.get_leshan_instance
	object_values = self.get_object_values
	for url, devices in leshan_instances(urls):
	    for device in devices:
	        for object in device['objectLinks']:
		    values = object_values(url, device['endpoint'], object['url'])
                    self.add_metadata(values, device, object)
	            self.__data.append(values)

    @staticmethod
    def get_leshan_instance(urls):
	for url in urls:
            response = get(url)
	    if response.status_code == codes.ok:
	        yield url, loads(response.text)

    @staticmethod
    def get_object_values(url, endpoint, obj_url):
	object_values = None

	request_url = url + sep + endpoint + obj_url
        response = get(request_url)

        if response.status_code == codes.ok:
            object_values = loads(response.text)

	return object_values

    @staticmethod
    def add_metadata(values, device, object):
	values['endpoint'] = device['endpoint']
	values['registrationId'] = device['registrationId']
	values['registrationDate'] = device['registrationDate']
	values['address'] = device['address']
	values['objectId'] = object['objectId']
	values['objectInstanceId'] = object['objectInstanceId']

    @property
    def data(self):
	return dumps(self.__data)

    def __str__(self):
	return self.data

if __name__ == "__main__":
    print LeshanPoller()


