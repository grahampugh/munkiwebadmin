#from django.db import models
import os
import plistlib

from django.conf import settings

# MUNKI_REPO_DIR is set to whatever the variable in MWA is, in settings.py
REPO_DIR = settings.MUNKI_REPO_DIR
random_variable = 'test'

# Read contents of all pkginfo files. You should be able to do this by reading the contents of catalogs/all

class Pkginfo(object):
    @classmethod
    def list(self):
        '''Returns a list of available pkgs, which is a list
        of pkg names (strings)'''
        all_catalog_path = os.path.join(REPO_DIR, 'catalogs/all')
        if os.path.exists(ALLCATALOG_PATH):
            try:
                all_catalog_items = plistlib.readPlist(all_catalog_path)
                index = 0
                for item in all_catalog_items:
                    item['index'] = index
                    index += 1
                return all_catalog_items
            except Exception, errmsg:
                return None
        else:
            return None

#    @classmethod
#    def edit(self):
#        '''Writes the changes of catalog to each pkginfo file'''

