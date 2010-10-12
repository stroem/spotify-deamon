#!/usr/bin/env python

import ConfigParser
import optparse
from session_manager import *

op = optparse.OptionParser(version="%prog 0.1")
op.add_option("-u", "--username", help="spotify username")
op.add_option("-p", "--password", help="spotify password")
(options, args) = op.parse_args()

username = options.username
password = options.password

if not options.username or not options.password:
	config = ConfigParser.ConfigParser()
	config.read("client.conf")
	username = config.get("spotify", "username")
	password = config.get("spotify", "password")
	#op.print_help()
	#raise SystemExit
	
s = SessionManager(username, password)
s.connect()
