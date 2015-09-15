from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from models import Pkginfo

import os

@login_required
def index(request):
    all_catalog_items = Pkginfo.list()
    random_variable = 'test'

    return render_to_response('pkginfo/index.html',
                              {'user': request.user,
                               'all_catalog_items': all_catalog_items,
                               'random_variable': random_variable,
                               }
                              )

