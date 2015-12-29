from django.shortcuts import render
from django.views import generic
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Languages, Menu, MenuInfo
from django.http import Http404

import json, simplejson
import time

class IndexViews(generic.View):
    templates_file = 'thanksIndex.html'

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


        groups = list(Group.objects.all().order_by('code'))
        if not groups:
            group_list = []
        else:
            group_list = []
            for g in groups:
                thanks = list(Thanks.objects.filter(group=g))
                if thanks:
                    thanks_list = []
                    for t in thanks:
                        b = {'name': t.name, 'url': t.url, 'img': t.img}
                        thanks_list.append(b)
                else:
                    thanks_list = []
                a = {'group': g.name, 'thanks_list': thanks_list}
                group_list.append(a)

        vthankss = list(VThanks.objects.all())
        if not vthankss:
            vthankss = []

        context = {
            'group_list': group_list,
            'vthankss': vthankss,
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
        }

        return render(request,
                      self.templates_file,
                      context)


# def get_version(request):
#     f = file('static/json/version.json')
#     source = f.read()
#     target = json.JSONDecoder().decode(source)
#     return HttpResponse(json.dumps(target))

def get_time(request):
    pubdate = time.strftime('%Y-%m-%d %H:%M:%s', time.localtime(time.time()))
    return HttpResponse(pubdate)