from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from models import Pkginfo

import os

@login_required
def index(request):
    pkginfo_list = Pkginfo.list()

    return render_to_response('pkginfo/index.html',
                            {'user': request.user})

