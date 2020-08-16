#!/usr/bin/python

from sys import argv

try: # i.e. if proper file creation argument is given.
	file_name = argv[argv.index("new") + 1]
	
except:
	pass
