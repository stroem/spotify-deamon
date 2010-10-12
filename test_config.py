#!/usr/bin/env python

############################
## READ CONFIG
############################
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("client.conf")

print config.get("spotify", "username")
print config.get("app", "version")

http_host = config.get("app", "callback_host")
http_site = config.get("app", "callback_site")

class Callable:

    def __init__(self, anycallable):
        self.__call__ = anycallable

class ConfigManager:
	
	_init = False
	
	def init(filename):
		ConfigManager._init = True
		config = ConfigParser.ConfigParser()
		config.read(filename)
		
		#for section in config.sections():
		#	print section
		#	for option in config.options(section):
		#		print " ", option, "=", config.get(section, option)

	def get(section, option):
		if ConfigManager._init == False:
			ConfigManager.init("client.conf")			
		return config.get(section, option)

	init = Callable(init)
	get = Callable(get)


ConfigManager.get("app", "version")

############################
## HTTP POSTS
############################
import httplib

connection = httplib.HTTPConnection(http_host)
connection.request("POST", "/" + http_site)
response = connection.getresponse()
if response.status == 200:
	data = response.read()
	print data
	
connection.close()

############################
## Remove *.pyc files
############################
import os

directory = os.listdir('.')
for filename in directory:
    if filename[-3:] == 'pyc':
        os.remove(filename)
