# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt
from home.models import Menu, MenuInfo, Languages
from django.http import Http404


import time
import datetime
import json, simplejson
import codecs
import re


class IndexViews(generic.View):
    templates_file = 'testing.html'

    def get(self, request):

        lang = request.LANGUAGE_CODE


        languages = list(Languages.objects.all())
        if not languages:
            languages = []


        dlangs = list(Languages.objects.filter(text=lang))
        if dlangs:
            dlang = dlangs.pop().id
        else:
            raise Http404


        menus = list(Menu.objects.all().order_by('sort'))
        if menus:
            menu_list = []
            for p in menus:
                menuinfos = list(MenuInfo.objects.filter(language=dlang, menu=p.id))
                if menuinfos:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                else:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                menu_list.append(a)
        else:
            menu_list = []


        platforms = list(Platform.objects.all().order_by("sort"))

        if platforms:
            platforms_list = []
            for p in platforms:
                versions = list(Versions.objects.filter(platform=p.id))
                if versions:
                    version_list = []
                    for q in versions:
                        versioninfos = list(VersionInfo.objects.filter(vs=q.id, language=dlang))
                        if versioninfos:
                            a = {"version": q.versions, "info": versioninfos.pop().info}
                        else:
                            a = {"version": q.versions, "info": ""}
                        version_list.append(a)
                    def version(s):
                        return s['version']
                    versioninfo_list = sorted(version_list, key=version, reverse=True)
                    print "v"
                    print versioninfo_list[0]
                    b = {"platform": p.code, 'img': p.img, 'url': p.url, 'version': p.version, "versioninfo": versioninfo_list, 'newversion': versioninfo_list[0]}
                    print b
                else:
                    b = {"platform": p.code, 'img': p.img, 'url': p.url, 'version': p.version, "versioninfo": [], 'newversion': ""}
                platforms_list.append(b)
        else:
            platforms_list = []


        f2 = file('static/json/android.json')
        source2 = f2.read()
        target2 = json.JSONDecoder().decode(source2)
        download_url = target2["url"]

        context = {
            "download_url": download_url,
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
            'platforms_list': platforms_list,
        }

        return render(request,
                      self.templates_file,
                      context)


class SuccessViews(generic.View):
    templates_file = 'success.html'

    def get(self, request):

        lang = request.LANGUAGE_CODE


        languages = list(Languages.objects.all())
        if not languages:
            languages = []


        dlangs = list(Languages.objects.filter(text=lang))
        if dlangs:
            dlang = dlangs.pop().id
        else:
            raise Http404


        menus = list(Menu.objects.all().order_by('sort'))
        if menus:
            menu_list = []
            for p in menus:
                menuinfos = list(MenuInfo.objects.filter(language=dlang, menu=p.id))
                if menuinfos:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                else:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                menu_list.append(a)
        else:
            menu_list = []

        if 'error' in request.GET and request.GET['error']:
            error_num = request.GET['error']
        else:
            error_num = ""

        context = {
            "error_num": error_num,
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
        }

        return render(request,
                      self.templates_file,
                      context)


class IOSViews(generic.View):
    templates_file = 'ios.html'

    def get(self, request):

        lang = request.LANGUAGE_CODE


        languages = list(Languages.objects.all())
        if not languages:
            languages = []


        dlangs = list(Languages.objects.filter(text=lang))
        if dlangs:
            dlang = dlangs.pop().id
        else:
            raise Http404


        menus = list(Menu.objects.all().order_by('sort'))
        if menus:
            menu_list = []
            for p in menus:
                menuinfos = list(MenuInfo.objects.filter(language=dlang, menu=p.id))
                if menuinfos:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                else:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                menu_list.append(a)
        else:
            menu_list = []

        context = {
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
        }

        return render(request,
                      self.templates_file,
                      context)


class ANDROIDViews(generic.View):
    templates_file = 'android.html'

    def get(self, request):

        lang = request.LANGUAGE_CODE


        languages = list(Languages.objects.all())
        if not languages:
            languages = []


        dlangs = list(Languages.objects.filter(text=lang))
        if dlangs:
            dlang = dlangs.pop().id
        else:
            raise Http404


        menus = list(Menu.objects.all().order_by('sort'))
        if menus:
            menu_list = []
            for p in menus:
                menuinfos = list(MenuInfo.objects.filter(language=dlang, menu=p.id))
                if menuinfos:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                else:
                    a = {"id": p.id, "url": p.url, "name": menuinfos.pop().name}
                menu_list.append(a)
        else:
            menu_list = []

        f = file('static/json/android.json')
        source = f.read()
        target = json.JSONDecoder().decode(source)
        download_url = target["url"]

        context = {
            "download_url": download_url,
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
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

    else:
        return HttpResponseRedirect('/beta/success?error=%d' % int(2))

    return HttpResponseRedirect('/beta/success?error=%d' % int(1))


# def download_AD(request):
#
#     f = file('static/json/android.json')
#     source = f.read()
#     target = json.JSONDecoder().decode(source)
#
#     return HttpResponse(target)
