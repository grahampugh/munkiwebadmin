#from django.db import models
import os
import plistlib

from django.conf import settings

# MUNKI_REPO_DIR is set to whatever the variable in MWA is, in settings.py
REPO_DIR = settings.MUNKI_REPO_DIR
all_catalog_path = os.path.join(REPO_DIR, 'catalogs/all')

if not os.path.exists(all_catalog_path):
    fail('Catalogs not accessible')

# Read contents of all pkginfo files. You should be able to do this by reading the contents of catalogs/all

all_catalog = plistlib.readPlist(all_catalog_path)

class Pkginfo(object):
    @classmethod
    def list(self):
        '''Returns a list of available pkgs, which is a list
        of pkg names (strings)'''

        index = 0
        for item in all_catalog:
            index = 0
            for item in catalog_items:
                item['index'] = index
                index += 1
            return catalog_items

#    @classmethod
#    def edit(self):
#        '''Writes the changes of catalog to each pkginfo file'''

