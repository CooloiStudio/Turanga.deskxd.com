from django.shortcuts import render
from django.views import generic
from models import *

class IndexViews(generic.View):
    templates_file = 'Index.html'

    def get(self, request):

        speciallist = list(Special.objects.all())
        if speciallist:
            specials = speciallist
        else:
            specials = []

        headerlist = list(SectionHeader.objects.all())
        if headerlist:
            sectionheaders = headerlist.pop()
        else:
            sectionheaders = []

        onelist = list(SectionOne.objects.all())
        if onelist:
            sectionones = onelist.pop()
        else:
            sectionones = []

        twolist = list(SectionTwo.objects.all())
        if twolist:
            sectiontwos = twolist.pop()
        else:
            sectiontwos = []

        threelist = list(SectionThree.objects.all())
        if threelist:
            sectionthrees = threelist.pop()
        else:
            sectionthrees = []


        context = {
            "specials": specials,
            "sectionheaders": sectionheaders,
            "sectionones": sectionones,
            "sectiontwos": sectiontwos,
            "sectionthrees": sectionthrees,
        }

        return render(request,
                      self.templates_file,
                      context)