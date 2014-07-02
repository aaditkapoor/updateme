from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotAllowed,Http404
from django.template import RequestContext
from .models import SiteSection
from Blogs.models import Blogs
from django.core.urlresolvers import reverse

def search_section(request):
    query = request.GET.get('q_section','')
    template_name = 'Search/found.html'
    query = query.lower()
    url_to_show = ''
    if request.method == 'GET':
        a = SiteSection()
        list_of_sections = [a.section1,a.section2,a.section3]
        if query in list_of_sections:
            if query == 'help':
                url_to_show = '/help/'
            elif query == 'contact':
                url_to_show = '/contact/'
            elif query == 'blogs':
                url_to_show = '/blogs/'
            main_url_link = '%s' % url_to_show
            name_of_url = '%s' % query
            return render_to_response(template_name,{
                'search_item': query,
                'status': True,
                'url_link': main_url_link,
                'url_name': name_of_url,
            })
        else:
            if query == '':
                return HttpResponse('No value given!')
            else:
                return render_to_response(template_name,{
                'search_item': query,
                'status': False
            })

def search_author(request):
    author_user = request.GET.get('q_author','')
    template_name = 'Search/author_found.html'
    author = author_user.lower()
    authors = Blogs.objects.filter(approved=True)
    search_item = ''
    if request.method == 'GET':
        for a in authors:
            if author == a.author:
                search_item = author
                break
            else:
                search_item = None
                continue

        if search_item is None:
            return render_to_response(template_name,
                {
                    'search_item': search_item,
                    'status': False
                })
        else:
            return render_to_response(template_name,
                {
                    'search_item': author,
                    'status': True,
                })
    else:
        return HttpResponse('<b>No value given!</b>')

def search_blog(request):
    if request.method == 'GET':
        key = request.GET.get('q_blog')
        return HttpResponseRedirect('/blog/show_by_blog/%d' % int(key))
    else :
        return HttpResponseRedirect(reverse('updateme.views.error',args=['ValueNotProvided']))





