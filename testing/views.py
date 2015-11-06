#encoding=utf8
from django.shortcuts import render
from django.views import generic
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage


from models import *
import re

class IndexViews(generic.View):
    templates_file = 'testing.html'

    def get(self, request):

        context = {
        }

        return render(request,
                      self.templates_file,
                      context)


class SuccessViews(generic.View):
    templates_file = 'success.html'

    def get(self, request):

        error_num = request.GET['error']

        context = {
            "error_num": error_num,
        }

        return render(request,
                      self.templates_file,
                      context)


class IOSViews(generic.View):
    templates_file = 'ios.html'

    def get(self, request):

        context = {
        }

        return render(request,
                      self.templates_file,
                      context)


class ANDROIDViews(generic.View):
    templates_file = 'android.html'

    def get(self, request):

        context = {
        }

        return render(request,
                      self.templates_file,
                      context)


def sendmessage(request):

    if 'email' in request.POST and request.POST['email']:
        email = request.POST['email']
    else:
        return HttpResponseRedirect('/beta/success?error=%d' % int(2))

    isemail = re.match(r'[A-Za-z0-9][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$', email)
    if isemail:
        users = list(UserMessage.objects.filter(email=email))
        if users:
            return HttpResponseRedirect('/beta/success?error=%d' % int(0))
        else:
            p = UserMessage(
                email=email
            )
            p.save()

            # # send-email
            mail_list = ["turanga@deskxd.com", ]
            send_mail(
                subject='新增用户邮箱',
                message=p.email,
                from_email='deskxd@outlook.com',
                recipient_list=mail_list,
                fail_silently=True
            )

    else:
        return HttpResponseRedirect('/beta/success?error=%d' % int(2))

    return HttpResponseRedirect('/beta/success?error=%d' % int(1))