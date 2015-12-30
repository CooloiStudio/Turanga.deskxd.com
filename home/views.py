from django.shortcuts import render, render_to_response
from django.views import generic
from home.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.template import RequestContext

import json
import simplejson

class IndexViews(generic.View):
    templates_file = 'Index.html'

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


        sections = list(Section.objects.all().order_by('sort'))
        if sections:
            section_list = []
            for p in sections:
                sectioninfos = list(SectionInfo.objects.filter(language=dlang, section=p.id))
                if sectioninfos:
                    for q in sectioninfos:
                        a = {"basepage": p.basepage.name, "img": p.img, "url": p.url, "title": q.title, "subtitle": q.subtitle, 'text': q.text, 'subtext': q.subtext}
                        section_list.append(a)
                else:
                    a = {"basepage": p.basepage.name, "img": p.img, "url": p.url, "title": "", "subtitle": "", "text": "", 'subtext': ""}
                    section_list.append(a)
        else:
            section_list = []


        context = {
            'languages': languages,
            'lang': lang,
            'menu_list': menu_list,
            'section_list': section_list
        }

        return render_to_response(
                self.templates_file,
                context,
                context_instance=RequestContext(request))