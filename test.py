#!/usr/bin/python

import os
import sys
import subprocess
import plistlib
import optparse
import fnmatch, re

findtext='fire'
matcher = "Firefox"
if fnmatch.fnmatch(matcher.lower(), findtext.lower()):
	print "Match"
else: print "No match"

all_catalog_path = '/Volumes/Images/vagrant/docker-munki/munki_repo/catalogs/all'
if os.path.exists(all_catalog_path):
	try:
		all_catalog_items = plistlib.readPlist(all_catalog_path)
		all_catalog_items = sorted(all_catalog_items, key=lambda x: (x['name'].lower(), x['version']))
		index = 0
		for item in all_catalog_items:
			item['index'] = index
			index += 1
		if findtext:
			filtered_list = []
			for item in all_catalog_items:
				if fnmatch.fnmatch(item['name'].lower(), findtext.lower()):
					filtered_list.append(item)
			print "Filtered list:"
			print filtered_list
		else:
			print "All the catalog:"
			print all_catalog_items
	except Exception, errmsg:
		print "Path Failed"
else:
	print "Failed"