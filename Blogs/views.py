import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from  django.contrib import messages
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from .models import Blogs, Error
from key import Key


def home(request):
    template_name = 'Blogs/index_blog.html'
    return render_to_response(template_name)


def process_data(request):
    author = request.GET.get('author')
    blog = request.GET.get('blog')
    date = datetime.datetime.now()
    email = request.GET.get('email')
    if request.method == 'GET':
        key = Key('m')
        code = key.generate()
        data = Blogs(author=author, blog=blog, date=date, unique_key=code, email=email)
        subject = 'Updateme: Blog ID: %d' % code
        message = 'Your Blog ID NUMBER %d has been sent for approving. Thank you!' % code
        send_mail(subject, message, 'akapoorx00@gmail.com', [email], fail_silently=False)
        data.save()
    else:
        return HttpResponse('Empty!')
    print author
    return HttpResponseRedirect('/blog/thank/%s' % request.GET.get('author'))


def retrieve(request):
    template_name = 'Blogs/latest.html'
    approved_data = Blogs.objects.filter(approved=True)
    if approved_data:
        return render_to_response(template_name,
                                  {
                                      'data': approved_data,
                                      'status': True
                                  })
    else:
        return render_to_response(template_name,
                                  {
                                      'status': False
                                  }
        )


# ---------------------------------Error reporting-----------------------------
def report_error(request):
    template_name = 'Blogs/report.html'
    return render_to_response(template_name, context_instance=RequestContext(request))


def report_forward(request):
    error = request.GET.get('error')
    return HttpResponseRedirect('%s' % error)


def error_report(request, error=None):
    errors = Error(error=error, date=datetime.datetime.now())
    errors.save()

    return render_to_response('Blogs/notify.html',
                              {
                                  'status': 'Our team is going through the problem.',
                              })


def get_solved_errors(request):
    solved = Error.objects.filter(resolved=True)
    return render_to_response('Blogs/report.html',
                              {
                                  'solved': solved,
                              })


# ------------------------


def show_blogs(request, user):
    blogs = Blogs.objects.filter(author__startswith=user, approved=True)
    return render_to_response('Blogs/show_blogs.html',
                              {
                                  'blogs': blogs,
                                  'user': user,
                              })


def thank(request, user):
    return render_to_response('Blogs/thank.html',
                              {
                                  'name': user
                              }
    )


def like(request):
    """
         like(request) -> int
         return the number of likes
     """
    key = request.GET.get('blog_id')
    Blog = Blogs.objects.get(unique_key=int(key))
    return HttpResponseRedirect('/blog/like_post/%d' % Blog.unique_key)


def like_post(request, key):
    blog_to_like = Blogs.objects.get(unique_key=int(key))
    blog_to_like.increment_like()
    blog_to_like.save()
    return HttpResponseRedirect('/blog/latest/')


def most_liked(request):
    blogs = Blogs.objects.filter(likes__gte=1).exclude(approved=False)

    # Algorithm to be re-checked
    largest = blogs[0].get_likes()
    key_to_show = 0
    for i in blogs:
        if i.get_likes >= largest:
            key_to_show = i.unique_key
            continue
    print key_to_show
    show = Blogs.objects.get(unique_key=key_to_show)
    message = 'Congrats, You are the winner, Your blogs has about %d likes, Congrats' % show.get_likes()
    return render_to_response('Search/most_liked.html',
                              {
                                  'show': show,

                              })


def show_by_blog(request, id):
    try:
        blog = Blogs.objects.get(unique_key=id)
    except:
        return HttpResponseRedirect(reverse('updateme.views.error', args=['ValueNotProvided']))
    else:
        return render_to_response('Blogs/blog_found.html',
                                  {
                                      'blog': blog
                                  })

