from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from models import Pkginfo
from catalogs.models import Catalog

import os

@login_required
def index(request):
    all_catalog_items = Pkginfo.detail()
    catalog_list = Catalog.list()
    if 'production' in catalog_list:
        catalog_name = 'production'
    elif 'standard' in catalog_list:
        catalog_name = 'standard'
    elif 'testing' in catalog_list:
        catalog_name = 'testing'
    else:
#        catalog_name = catalog_list[0]
        catalog_name = 'none'
    return render_to_response('pkginfo/index.html',
                              {'user': request.user,
                               'all_catalog_items': all_catalog_items,
                               'catalog_list': catalog_list,
                               'catalog_name': catalog_name,
                               }
                              )



# @login_required
# def item_detail(request, item_index):
#     catalog_item = Pkginfo.item_detail(item_index)
#     featured_keys = ['name', 'version', 'catalogs']
#     # sort the item by key so keys are displayed
#     # in expected order
#     sorted_dict = SortedDict()
#     for key in featured_keys:
#         if key in catalog_item:
#             sorted_dict[key] = catalog_item[key]
#     key_list = catalog_item.keys()
#     key_list.sort()
#     for key in key_list:
#         if key not in featured_keys:
#             sorted_dict[key] = catalog_item[key]
#     return render_to_response('pkginfo/index.html', 
#                               {'catalog_item': sorted_dict})
#                               
