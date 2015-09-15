#from django.db import models
import os
import plistlib

from django.conf import settings

# MUNKI_REPO_DIR is set to whatever the variable in MWA is, in settings.py
REPO_DIR = settings.MUNKI_REPO_DIR

# Read contents of all pkginfo files. You should be able to do this by reading the contents of catalogs/all

class Pkginfo(object):
    @classmethod
    def detail(self):
        '''Returns a list of available pkgs, which is a list
        of pkg names (strings)'''
        all_catalog_path = os.path.join(REPO_DIR, 'catalogs/all')
        if os.path.exists(all_catalog_path):
            try:
                all_catalog_items = plistlib.readPlist(all_catalog_path)
                all_catalog_items = sorted(all_catalog_items, key=lambda x: (x['name'].lower(), x['version']))
                index = 0
                for item in all_catalog_items:
                    item['index'] = index
                    index += 1
                return all_catalog_items
            except Exception, errmsg:
                return None
        else:
            return None

#     @classmethod
#     def item_detail(self, item_index):
#         '''Returns detail for a single pkg'''
#         all_catalog_path = os.path.join(
#             REPO_DIR, 'catalogs/all')
#         if os.path.exists(all_catalog_path):
#             try:
#                 all_catalog_items = plistlib.readPlist(all_catalog_path)
#                 return all_catalog_items[int(item_index)]
#             except Exception, errmsg:
#                 return None
#         else:
#             return None


