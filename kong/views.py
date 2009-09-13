# Create your views here.

from kong.models import TestResult, Test
from kong.utils import get_latest_results
from kong.models import Site, Type, Server
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import list_detail

def index(request):
    ret_val = []
    for site in Site.objects.all():
        results = get_latest_results(site)
        ret_val.extend(results)

    return render_to_response('kong/index.html',
                       {'results': ret_val},
                       context_instance=RequestContext(request))

def site_list(request):
    qs = Site.objects.all()
    return list_detail.object_list(request, qs)

def site_object(request, site_slug):
    ret_val = []
    sites = Site.objects.filter(slug=site_slug)
    for site in sites:
        results = get_latest_results(site)
        ret_val.extend(results)

    return render_to_response('kong/index.html',
                       {'results': ret_val},
                       context_instance=RequestContext(request))

def test_list(request):
    qs = Test.objects.all()
    return list_detail.object_list(request, qs)

def test_object(request, test_slug):
    test = Test.objects.get(slug=test_slug)
    tests = TestResult.objects.filter(test=test)
    return render_to_response('kong/testresult_detail.html',
                       {'results': tests },
                       context_instance=RequestContext(request))

def type_list(request):
    qs = Type.objects.all()
    return list_detail.object_list(request, qs)

def type_object(request, type_slug):
    type = Type.objects.get(slug=type_slug)
    sites = type.sites.all()
    ret_val = []
    for site in sites:
        results = get_latest_results(site)
        ret_val.extend(results)

    return render_to_response('kong/index.html',
                       {'results': ret_val },
                       context_instance=RequestContext(request))


def server_list(request):
    qs = Server.objects.all()
    return list_detail.object_list(request, qs)

def server_object(request, server_slug):
    server = Server.objects.get(slug=server_slug)
    sites = server.sites.all()
    ret_val = []
    for site in sites:
        results = get_latest_results(site)
        ret_val.extend(results)

    return render_to_response('kong/index.html',
                       {'results': ret_val },
                       context_instance=RequestContext(request))