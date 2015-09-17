from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django import forms

from models import Pkginfo
from catalogs.models import Catalog

import os
import csv

@login_required
def index(request):
    all_catalog_items = Pkginfo.detail()
    catalog_list = Catalog.list()
    catalog_name = 'none'
    if 'production' in catalog_list:
        catalog_name = 'production'
    elif 'standard' in catalog_list:
        catalog_name = 'standard'
    elif 'testing' in catalog_list:
        catalog_name = 'testing'
    return render_to_response('pkginfo/index.html',
                              {'user': request.user,
                               'all_catalog_items': all_catalog_items,
                               'catalog_list': catalog_list,
                               'catalog_name': catalog_name,
                               })

@csrf_exempt
def confirm(request):
    if request.method == 'POST': # If the form has been submitted...
        dest_catalog = request.POST.get('dest_catalog')
        items_to_move = request.POST.getlist('items_to_move[]')
        source_catalogs = request.POST.getlist('source_catalogs[]')
        tuple(source_catalogs)
        tuple(items_to_move)
        for n,pkg in enumerate(items_to_move):
            pkg = pkg.split('___')
            items_to_move[n] = pkg
        for m,pkgm in enumerate(source_catalogs):
            pkgm = pkgm.split('___')
            source_catalogs[m] = pkgm
        items_to_actually_move = ()
        for namecheck, versioncheck in items_to_move:
            for a,b,c in source_catalogs:
                if namecheck == a and versioncheck == b:
                    if c != dest_catalog and items_to_actually_move == ():
                        items_to_actually_move = items_to_actually_move, ( a, b, c )
                    elif c != dest_catalog:
                        items_to_actually_move = ( a, b, c )
        c = {'user': request.user,
             'dest_catalog': dest_catalog,
             'items_to_actually_move': items_to_actually_move}
        return render_to_response('pkginfo/confirm.html', 
                                  c)
    else:
        return HttpResponse("No form submitted.\n")


        # for each item in checked
            # split back to version and string
            # look up path to file in catalog details
            # edit catalogs field in the file
            # set a variable to state that something has changed
        # if something has changed, makecatalogs
