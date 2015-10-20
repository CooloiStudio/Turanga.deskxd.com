from django.shortcuts import render
from django.views import generic
from models import *
from django.http import HttpResponse, HttpResponseRedirect

class IndexViews(generic.View):
    templates_file = 'thanksIndex.html'

    def get(self, request):

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
        }

        return render(request,
                      self.templates_file,
                      context)