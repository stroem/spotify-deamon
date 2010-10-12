#!/usr/bin/env python
import sys
sys.path.append("src/")

import optparse
from session_manager import *

op = optparse.OptionParser(version="%prog 0.1")
op.add_option("-u", "--username", help="spotify username")
op.add_option("-p", "--password", help="spotify password")
(options, args) = op.parse_args()

if not options.username or not options.password:
	op.print_help()
	raise SystemExit
	
s = SessionManager(options.username, options.password)
s.connect()
