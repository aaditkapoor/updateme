from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from django.utils import timezone


def information(request):
    return {
        'creator': 'Aadit Kapoor',
        'Browser': request.path,
        'Version': '1.0.0.0,'
    }


def home(request):
    """ Main page of the webiste"""
    template_name = 'index.html'
    date = timezone.now()
    return render_to_response(template_name, {'date': date}, RequestContext(request, processors=[information]))


def process_error(request, error_q):
    return render_to_response('Error_Pages/index.html',
                              {
                                  'error': error_q,
                              })
