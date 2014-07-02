from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone, termcolors
from .models import Helping
from django.utils import feedgenerator
def b_info(request):
    return {
        'date': timezone.now(),
        'welcome_msg': 'Welcome to Help!',
        'pages': [1,2,3],
    }


def home(request):
    template_name = 'Helper/index_help.html'
    return render_to_response(template_name,RequestContext(request,processors=[b_info]))

def introduction(request):
    template_name = 'Helper/intro/intro.html'
    return render_to_response(template_name,
        {
            'path': request.path,
        },
        RequestContext(request,processors=[b_info])
    )

def submit_feature(request):
    return render_to_response('Helper/submit_feature/submit.html', RequestContext(request))

def process_feature(request):
    return render_to_response('Helper/submit_feature/thank.html')




