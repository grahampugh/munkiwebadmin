from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django import forms

from models import Pkginfo
from catalogs.models import Catalog

import os
import csv

@csrf_protect
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

@csrf_protect
def confirm(request):
    context = {}
    request_context = RequestContext(request)
    if request.method == 'POST': # If the form has been submitted...
        dest_catalog = request.POST.get('catalog')
        checked_pkgs = request.POST.getlist('items_to_move[]')
        checked_pkg_names = []
        checked_pkg_versions = []
        for pkg in checked_pkgs:
            tuple(pkg.split('_'))
    return render_to_response('pkginfo/confirm.html', 
                              request_context,
                              {'user': request.user,
                               'dest_catalog': dest_catalog,
                               'checked_pkgs': checked_pkgs,
                               })


        # for each item in checked
            # split back to version and string
            # look up path to file in catalog details
            # edit catalogs field in the file
            # set a variable to state that something has changed
        # if something has changed, makecatalogs
