#encoding=utf8
from django.shortcuts import render
from django.views import generic
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
import time
import datetime
import json

from models import *
import re

class IndexViews(generic.View):
    templates_file = 'testing.html'

    def get(self, request):

        f = file('static/json/version.json')
        source = f.read()
        target = json.JSONDecoder().decode(source)

        print target["version"]["android"]

        context = {
            "android_v": target["version"]["android"],
            "ios_v": target["version"]["ios"]
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

        f = file('static/json/android.json')
        source = f.read()
        target = json.JSONDecoder().decode(source)
        download_url = target["url"]

        context = {
            "download_url": download_url
        }

        return render(request,
                      self.templates_file,
                      context)

class ADViews(generic.View):
    templates_file = 'ad.html'

    def get(self, request):

        f = file('static/json/android.json')
        source = f.read()
        target = json.JSONDecoder().decode(source)
        download_url = target["url"]

        context = {
            "download_url": download_url
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
            pub_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            p = UserMessage(
                email=email,
                datatime=pub_date
            )
            p.save()

            print datetime.datetime.now()

            # mail_list = ["turanga@deskxd.com", ]
            # send-email
            # try:
            #     send_mail(
            #         subject='新增用户邮箱',
            #         message=p.email,
            #         from_email='deskxd@outlook.com',
            #         recipient_list=mail_list,
            #         fail_silently=True
            #     )
            # except Exception, e:
            #     print str(e)

    else:
        return HttpResponseRedirect('/beta/success?error=%d' % int(2))

    return HttpResponseRedirect('/beta/success?error=%d' % int(1))