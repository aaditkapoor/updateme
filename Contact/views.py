
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from ipware.ip import get_ip
import datetime
from django.http import HttpResponseServerError
from django.core.mail import send_mail,send_mass_mail
from reply import data as reply
from django.utils import timezone
from django.core.urlresolvers import  reverse
from .models import Contact
def home(request):
    template_name = 'Contact/index_contact.html'
    return render_to_response(template_name,
        {
        },context_instance = RequestContext(request))

def thank_you(request):
    return render_to_response('Contact/thank.html')

def contact_request(request):
    try:
        phone_number = request.POST.get('phone_contact')
        email = request.POST.get('email_contact')
        message = request.POST.get('message_contact')
        date = timezone.now()
        uploaded_file = request.POST.get('upload')
        request.session['email'] = email
        request.session['message'] = message
    except ValueError:
        return HttpResponse('Error: In saving! Please check all fields')
    else:
        contact_user = Contact(email = email,phone_number = phone_number,message = message,date = date,notified=False)
        contact_user.save()
        request.session['check'] = True

    return HttpResponseRedirect('/contact/notify_by_email%s' % phone_number)

def notify_by_email(request,phone_number):
        email_to_send = request.session['email']
        message = request.session['message']

        key = reply.exists(message)
        if key is not None:
            available_replies = reply.generate(key)
            message_to_send = reply.get_reply(available_replies)

        try:
            send_mail('Updateme',message_to_send,'akapoorx00@gmail.com',[email_to_send],fail_silently=False)
            request.session['email_sent'] = True
        except:
            return HttpResponse('Cannot proceed further! Email error!')
        else:
            return HttpResponseRedirect(reverse('Contact.views.thank_you',args=[phone_number]))
